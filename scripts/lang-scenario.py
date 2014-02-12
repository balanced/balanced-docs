#!/usr/bin/env python
"""
Backend for the scenario dcode rST directive.

For example:

    .. dcode: scenario
        ...

Maps to:

    def main():
        ...

"""
import argparse
import contextlib
import errno
import json
import logging
import os
import pipes
import re
import requests
import shlex
import subprocess
import sys
import urllib

import balanced
import mako.lookup
import mako.template

from balanced_docs import (
    LogLevelAction,
    EnvironmentVarAction,
    dockers,
    BlockWriter,
    rev1_api_spec,
)


logger = logging.getLogger(__name__)

class basic_client(dict):
    def __init__(self, dictionary):
        self.update(**dictionary)
        for k, v in dictionary.items():
            try:
                setattr(self, k, v)
            except Exception as e:
                pass

class Context(object):

    def __init__(self,
            api_location,
            scenarios_dir,
            client_dir,
            storage_file,
            spec_file,
            langs,
            api_dir,
        ):
        self.stack = []
        self.api_location = api_location
        self.scenarios_dir = scenarios_dir
        self.client_dir = client_dir
        self.template_lookup = mako.lookup.TemplateLookup(
            directories=[scenarios_dir]
        )
        self.storage = Storage(
            storage_file,
            backfill=self.backfill_scenario,
        )
        self.rev = os.environ.get('BALANCED_REV', 'rev0')
        self.spec = dockers.load(open(spec_file, 'r'))
        self.langs = ['curl'] + langs

    def lookup_scenario(self, name):
        munged = name.replace('-', '_')
        path = os.path.join(self.scenarios_dir, munged)
        if not os.path.isdir(path):
            raise LookupError(
                'No scenario for "{0}" @ "{1}"'.format(name, path)
            )
        logger.debug('located scenario "%s" @ "%s"', name, path)
        return Scenario(self, path)

    def backfill_scenario(self, name):
        if self.scenario.name != name:
            try:
                scenario = self.lookup_scenario(name)
            except LookupError:
                logger.debug('no scenario "%s" to backfill', name)
            else:
                logger.debug('backfilling scenario "%s"', scenario.name)
                scenario()

    @property
    def marketplace(self):
        resp = requests.get(self.storage['api_location'] + self.storage['marketplace_uri'],
                                         headers={'Accept-Type': self.storage.get('accept_type', '*/*')},
                                         auth=(self.storage['secret'], ''))
        ret = basic_client(resp.json())
        #import ipdb; ipdb.set_trace()
        return ret

    @property
    def card(self):
        resp = requests.get(self.storage['api_location'] + self.storage['card_uri'],
                                         headers={'Accept-Type': self.storage.get('accept_type','*/*')},
                                         auth=(self.storage['secret'], ''))
        ret = basic_client(resp.json())
        return ret

    def __getattr__(self, k):
        if k in self.storage:
            return self.storage[k]
        raise AttributeError(
            "'{0}' object has no attribute '{1}'"
            .format(self.__class__.__name__, k)
        )

    @property
    def scenario(self):
        return self.stack[-1]

    def __call__(self, scenario):
        self.stack.append(scenario)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stack.pop()


class JSONSerializer(object):

    _ERROR_MSG = 'Object of type {0} with value of {1} is not JSON serializable'

    def __init__(self, explicit_none_check=False):
        self.serialization_chain = []
        self.explicit_none_check = explicit_none_check
        self.add(self._datetime)
        self.add(self._Resource)

    def add(self, callable_serializer):
        self.serialization_chain.append(callable_serializer)
        return self

    def __call__(self, serializable):
        for serializer in self.serialization_chain:
            result = serializer(serializable)
            if ((not self.explicit_none_check and result) or
                (self.explicit_none_check and result is not None)):
                return result
        error_msg = self.ERROR_MSG.format(
            type(serializable),
            repr(serializable),
        )
        raise TypeError(error_msg)

    @staticmethod
    def _datetime(serializable):
        if hasattr(serializable, 'isoformat'):
            # ttp://www.ietf.org/rfc/rfc3339.txt
            return serializable.isoformat() + 'Z'

    @staticmethod
    def _Resource(serializable):
        if not isinstance(serializable, balanced.Resource):
            return None
        return serializable.__dict__


class Storage(dict):

    json_serializer = JSONSerializer()

    def __init__(self, file_path, backfill):
        super(Storage, self).__init__()
        self.file_path = file_path
        self.backfill = backfill
        self._load()

    def _load(self):
        try:
            with open(self.file_path, 'r') as f:
                self.update(json.load(f))
        except IOError, ex:
            if ex.errno != errno.ENOENT:
                raise
            pass

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(
                self,
                f,
                sort_keys=True,
                indent=4,
                default=self.json_serializer
            )

    def __missing__(self, name):
        self.backfill(name)
        if name in self:
            return self[name]
        raise KeyError(name)


class Endpoint(object):

    def __init__(self, ctx, name, select=None):
        match = self._match(ctx, name, select)
        logger.debug('matched "%s" (%s)', name, select)
        self.ctx = ctx
        self.name = match['name']
        self.methods = match['methods']
        self.method = filter(lambda x: x not in ['HEAD', 'OPTIONS'], match['methods'])[0]
        self.uri = match['path']

    @classmethod
    def qualify_uri(cls, ctx, uri, **qs):
        url = ctx.storage['api_location'] + uri
        if qs:
            url += '?' + urllib.urlencode(qs)
        return url

    def format(self, **kwargs):
        args, params = {}, {}
        matches = re.findall(r':(\w+)', self.uri)
        if matches:
            fmt = re.sub(r':(\w+)', r'{\1}', self.uri)
            for k, v in kwargs.iteritems():
                if k in matches:
                    args[k] = v
                else:
                    params[k] = v
        else:
            fmt = self.uri
            args = kwargs
        uri = fmt.format(**args)
        if params:
            uri += '?' + urllib.urlencode(params)
        url = self.qualify_uri(self.ctx, uri)
        return url

    @property
    def url(self):
        return self.ctx.storage['api_location'] + self.uri

    @classmethod
    def _match(cls, ctx, name, select=None):
        matches = ctx.spec.match_endpoint(name)
        if not matches:
            raise LookupError('No endpoint matching "{0}"'.format(name))
        if len(matches) == 1:
            return matches[0]
        if not select:
            raise ValueError('Multiple endpoints matching "{0}" -- '
                '"{1}"'.format(name, '\n'.join([str(m) for m in matches])))
        if select == 'any':
            return matches[0]
        elif select == 'shortest':
            return min(matches, key=lambda m: len(m['path']))
        elif select == 'longest':
            return max(matches, key=lambda m: len(m['path']))
        elif isinstance(select, (list, tuple)):
            select = set(select)
            for match in matches:
                re_matches = set(re.findall(r':(\w+)', match['path']))
                if re_matches == select:
                    return match
            else:
                raise ValueError(
                    'No matches for {0}'
                    .format(', '.join('"{0}"'.format(s) for s in select))
                )
        raise ValueError('Unsuported policy "{0}"'.format(select))


class Scenario(object):

    @classmethod
    def bootstrap(cls, ctx):
        # api conf
        if ctx.storage.get('api_location') != ctx.api_location:
            ctx.storage.clear()
        if ctx.storage.get('api_rev') != os.environ.get('BALANCED_REV', 'rev0'):
            ctx.storage.clear()
        if 'api_key' not in ctx.storage:
            ctx.storage.clear()
            ctx.storage['api_location'] = ctx.api_location
            ctx.storage['api_rev'] = os.environ.get('BALANCED_REV', 'rev0')
            if ctx.storage['api_rev'] != 'rev0':
                ctx.storage['accept_type'] = {
                    'rev1': 'application/vnd.api+json;revision=1.1',
                }[ctx.storage['api_rev']]
            logger.debug('creating api key')
            #key = balanced.APIKey().save()
            #ctx.storage['api_key'] = key.secret
            key = requests.post(ctx.storage['api_location'] + ('/v1/api_keys' if ctx.storage['api_rev'] == 'rev0' else '/api_keys'),
                                headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')}
            )
            #import ipdb; ipdb.set_trace()
            if os.environ.get('BALANCED_REV') == 'rev1':
                secret = key.json()['api_keys'][0]['secret']
            else:
                secret = key.json()['secret']
            ctx.storage['secret'] = ctx.storage['api_key'] = secret

        balanced.config.root_uri = ctx.storage['api_location']
        balanced.configure(ctx.storage['api_key'])

        # marketplace
        if 'marketplace_id' not in ctx.storage:
            logger.debug('creating marketplace')
            marketplace = requests.post(ctx.storage['api_location'] + ('/v1/marketplaces' if ctx.storage['api_rev'] == 'rev0' else '/marketplaces'),
                                        headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                                        auth=(ctx.storage['secret'], '')
            )
            if os.environ.get('BALANCED_REV') == 'rev1':
                mp = marketplace.json()['marketplaces'][0]
                ctx.storage['marketplace_uri'] = mp['href']
                ctx.storage['marketplace_id'] = mp['id']
                ctx.storage['marketplace'] = basic_client(mp)
                ctx.storage['customers_uri'] = marketplace.json()['links']['marketplaces.customers']
            else:
                ctx.storage['marketplace_uri'] = marketplace.json()['uri']
                ctx.storage['marketplace_id'] = marketplace.json()['id']
                ctx.storage['marketplace'] = basic_client(marketplace.json())
            # marketplace = balanced.Marketplace().save()
            # ctx.storage['marketplace_uri'] = marketplace.uri
            # ctx.storage['marketplace_id'] = marketplace.id
        #    ctx.storage['marketplace_uri'] = 'TODO'
        #    ctx.storage['marketplace_id'] = 'TODO'

        # card
        if 'card_id' not in ctx.storage:
            logger.debug('creating card')
            card_data = {
                'name': 'Benny Riemann',
                'card_number' if ctx.storage['api_rev'] == 'rev0' else 'number': '4111111111111111',
                'expiration_month': 4,
                'expiration_year': 2016,
                'security_code': 323,
                'address[street_address]': '167 West 74th Street',
                'address[postal_code]': '10023',
                'address[country_code]': 'USA',
            }
            # card = ctx.marketplace.create_card()
            # ctx.marketplace.create_buyer(None, card.uri)
            # ctx.storage['card_uri'] = card.uri
            # ctx.storage['card_id'] = card.id


            customer = requests.post(ctx.storage['api_location'] + ('/v1/customers' if ctx.storage['api_rev'] == 'rev0' else '/customers'),
                                     headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                                     auth=(ctx.storage['secret'], ''))



            if os.environ.get('BALANCED_REV') == 'rev1':
                ctx.storage['customer'] = basic_client(customer.json())['customers'][0]
                links = customer.json()['links']
                ctx.storage['cards_uri'] = links['customers.cards'].replace('{customers.id}', ctx.storage['customer']['id'])
                cards_uri = ctx.storage['cards_uri']
            else:
                ctx.storage['customer'] = basic_client(customer.json())
                cards_uri = ctx.storage['customer'].cards_uri

            card = requests.post(ctx.storage['api_location'] + cards_uri,
                                 headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                                 auth=(ctx.storage['secret'], ''),
                                 data=card_data
            )

            if os.environ.get('BALANCED_REV') == 'rev1':
                # is this even used?
                ctx.storage['card_uri'] = card.json()['cards'][0]['href']
                ctx.storage['card_id'] = card.json()['cards'][0]['id']
                ctx.storage['card'] = basic_client(card.json()['cards'][0])
            else:
                ctx.storage['card_uri'] = card.json()['uri']
                ctx.storage['card_id'] = card.json()['id']
                ctx.storage['card'] = basic_client(card.json())


        marketplace_req = requests.get(ctx.storage['api_location'] + ctx.storage['marketplace_uri'],
                                       headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                                       auth=(ctx.storage['secret'], ''))

        if os.environ.get('BALANCED_REV') == 'rev1':
            marketplace = basic_client(marketplace_req.json()['marketplaces'][0])
        else:
            marketplace = basic_client(marketplace_req.json())
        # escrow
        thresh_h, thresh_l = 10000000, 100000
        if marketplace.in_escrow < thresh_l:
            amount = thresh_h - marketplace.in_escrow
            logger.debug('incrementing escrow balanced %s', amount)
            if os.environ.get('BALANCED_REV') == 'rev1':
                debits_uri = customer.json()['links']['customers.debits'].replace('{customers.id}', ctx.storage['customer']['id'])
            else:
                debits_uri = ctx.storage['customer'].debits_uri
            debit = requests.post(ctx.storage['api_location'] + debits_uri,
                                  headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                                  auth=(ctx.storage['secret'], ''),
                                  data={
                                      'amount': amount
                                  })
            ctx.storage['debit'] = basic_client(debit.json())

    def __init__(self, ctx, path):
        self.ctx = ctx
        self.name = os.path.basename(path)
        self.path = path
        self.definition = None
        self.request = None

    @property
    def metadata(self):
        if (self.name not in self.ctx.storage or
            'request' not in self.ctx.storage[self.name]):
            context = {
                'json': json,
                'ctx': self.ctx,
                'storage': self.ctx.storage,
                'marketplace': None #self.ctx.marketplace,
            }
            metadata = os.path.join(self.path, 'metadata.py')
            execfile(metadata, context, context)
            self.ctx.storage[self.name]['request'] = context['request']
        return self.ctx.storage[self.name]['request']

    def __call__(self):
        blocks = []
        curl = None
        self.ctx.storage[self.name] = {}
        with self.ctx(self):
            for lang in self.ctx.langs:
                block = self.block(lang)
                if not block:
                    continue
                if lang == 'curl':
                    curl = block
                blocks.append(block)
        response = curl.get('response') if curl else None
        return blocks, response

    def block(self, lang):
        if lang not in self.ctx.langs:
            return None
        template_path = os.path.join(self.path, lang + '.mako')
        if lang in ['php', 'ruby', 'node', 'python']:
            template_path = os.path.join(self.ctx.client_dir, os.environ.get('BALANCED_REV', 'rev0'), lang,
                                         'scenarios', self.name, lang+'.mako')
        if lang == 'java':
            template_path = os.path.join(self.ctx.client_dir, os.environ.get('BALANCED_REV', 'rev0'), lang, 'src',
                                         'scenarios', self.name, lang+'.mako')
        block = self._render(template_path)
        block['lang'] = lang
        if block['lang'] == 'curl':
            if 'delete' in self.name:
                logger.info('skipping execution for "%s" (%s)', self.name, block['lang'])
            else:
                block['response'] = json.dumps(
                    # delete returns nothing
                    json.loads(self._exec(block['request']) or '{}'),
                    indent=4,
                    sort_keys=True,
                )
                self.ctx.storage[self.name]['response'] = block['response']
        return block

    def _render(self, template_path):
        if 'api.balancedpayments.com' in self.ctx.storage['api_location']:
            api_location = None
        else:
            api_location = self.ctx.storage['api_location']
        context = {
            'ctx': self.ctx,
            'Endpoint': Endpoint,
            'api_location': api_location,
            'api_key': self.ctx.api_key,
        }
        context.update(request=self.metadata)

        # definition
        logger.debug('rendering definition for "%s"', template_path)
        template = mako.template.Template(
            filename=template_path,
            lookup=self.ctx.template_lookup
        )
        try:
            definition = template.render(mode='definition', **context).strip()
        except Exception:
            print mako.exceptions.text_error_template().render()
            raise

        # request
        logger.debug('rendering request for "%s"', template_path)
        if 'payload' in context['request']:
            context['payload'] = context['request']['payload']
        template = mako.template.Template(
            filename=template_path,
            lookup=self.ctx.template_lookup
        )
        try:
            request = template.render(mode='request', **context).strip()
        except Exception:
            print mako.exceptions.text_error_template().render()
            raise

        # response
        logger.debug('rendering response for "%s"', template_path)
        template = mako.template.Template(
            filename=template_path,
            lookup=self.ctx.template_lookup
        )
        try:
            response = template.render(mode='response', **context).strip()
        except Exception:
            print mako.exceptions.text_error_template().render()
            raise

        return {
            'definition': definition,
            'request': request,
            'response': response
        }

    def _exec(self, cmd):
        def is_quotable_character(s):
            return s.strip() not in ['\n', '']

        cmd = filter(
            is_quotable_character,
            shlex.split(cmd.encode('utf-8'))
        )
        sh_cmd = ' '.join(pipes.quote(p) for p in cmd)
        logger.debug('executing - %s', sh_cmd)
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            print >>sys.stderr, sh_cmd, '- exit code', proc.returncode
            print >>sys.stderr, 'stderr:'
            print >>sys.stderr, stderr
            print >>sys.stderr, 'stdout:'
            print >>sys.stderr, stdout
            raise Exception(
                '{0} - failed with exit code {1}'
                .format(sh_cmd, proc.returncode)
            )
        return stdout


@contextlib.contextmanager
def _mark_section(writer, section_name):
    begin_annotation = '.. begin-section: {0}\n\n'.format(section_name)
    end_annotation = '.. end-section: {0}\n\n'.format(section_name)

    writer(begin_annotation)
    yield
    writer(end_annotation)


def generate(write, name, blocks, response, section_chars):
    pygments = {
        'curl': 'bash',
    }

    with _mark_section(write, 'definition'):
        write('.. container:: definition\n\n')
        with write:
            write('Definition\n\n')
            for block in blocks:
                pygment = pygments.get(block['lang'], block['lang'])
                write('.. code-block:: {0}\n'.format(pygment))
                write('\n')
                with write:
                    write(block['definition'])
                write('\n\n')

    with _mark_section(write, 'request'):
        write('.. container:: request\n\n')
        with write:
            write('Example Request\n\n')
            for block in blocks:
                pygment = pygments.get(block['lang'], block['lang'])
                write('.. code-block:: {0}\n'.format(pygment))
                write('\n')
                with write:
                    write(block['request'])
                write('\n\n')

    if response:
        with _mark_section(write, 'response'):
            write('.. container:: response\n\n')
            with write:
                write('Example Response\n\n')
                write('.. code-block:: {0}\n'.format('javascript'))
                write('\n')
                with write:
                    write(response)
                write('\n\n')


# main

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'scenarios',
        nargs='+',
        metavar='SCENARIO',
        help='Name of the SCENARIO to run.',
    )
    parser.add_argument(
        '-l', '--log-level',
        choices=['debug', 'info', 'warn', 'error'],
        default=logging.INFO,
        action=LogLevelAction,
    )
    parser.add_argument(
        '-c', '--cache',
        metavar='PATH',
        default=None,
        help='PATH to scenario context cache file. No caching by default.',
    )
    parser.add_argument(
        '--sections',
        metavar='CHARS',
        default='~^',
        help='String of CHARS to use for section headings.',
    )
    parser.add_argument(
        '--api-location',
        metavar='URL',
        action=EnvironmentVarAction,
        env_var='BALANCED_DOCS_API_LOC',
        default='https://api.balancedpayments.com',
        help='Uses URL as the api location.',
    )
    parser.add_argument(
        '-s', '--storage',
        metavar='FILE',
        default='./scenario.cache',
        help='Storage FILE location',
    )
    parser.add_argument(
        '-d', '--directory',
        metavar='DIRECTORY',
        default='./scenarios',
        help='DIRECTORY containing named scenarios',
    )
    parser.add_argument(
        '--client',
        metavar='CLIENT',
        default='./clients',
        help='Directory containing the CLIENT submodules'
    )
    parser.add_argument(
        '-p', '--spec',
        metavar='FILE',
        default='balanced.json',
        help='FILE containing spec data',
    )
    # parser.add_argument(
    #     '--api',
    #     metavar='DIRECTORY',
    #     default='./balanced-api',
    #     dest='api_dir',
    #     help='Directory containing balanced-api'
    # )
    parser.add_argument(
        '--lang',
        metavar='LANGUAGE',
        dest='langs',
        action='append',
        default=[],
        choices=['php', 'python', 'ruby', 'java'],
        help='Enable LANGUAGE for the scenario',
    )
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    root = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    root.addHandler(handler)
    root.setLevel(args.log_level)

    ctx = Context(
        api_location=os.environ.get('BALANCED_API_LOC', args.api_location),
        scenarios_dir=os.path.abspath(args.directory),
        client_dir=os.path.abspath(args.client),
        storage_file=args.storage,
        spec_file=args.spec,
        langs=args.langs,
        api_dir=os.path.abspath('./balanced-api'),
    )
    Scenario.bootstrap(ctx)
    write = BlockWriter(sys.stdout)
    for scenario in args.scenarios:
        if os.environ.get('BALANCED_REV', 'rev0') != 'rev0':
            if re.match('^account_', scenario):
            #if 'account' in scenario.replace('bank_account', '') and False:
            # TODO: make this work
                with open('./empty-scenario', 'r') as some_file:
                    print some_file.read()
                continue
        logger.debug('scenario "%s"', scenario)
        scenario = ctx.lookup_scenario(scenario)
        blocks, response = scenario()
        generate(write, scenario.name, blocks, response, args.sections)
    ctx.storage.save()

if __name__ == '__main__':
    main()
