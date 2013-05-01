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
import errno
import json
import logging
import os
import pipes
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
)


logger = logging.getLogger(__name__)


class Context(object):

    def __init__(self,
            api_location,
            scenarios_dir,
            storage_file,
            spec_file,
            langs,
            execute_langs,
        ):
        self.stack = []
        self.api_location = api_location
        self.scenarios_dir = scenarios_dir
        self.template_lookup = mako.lookup.TemplateLookup(
            directories=[scenarios_dir]
        )
        self.storage = Storage(
            storage_file,
            backfill=self.backfill_scenario,
        )
        self.spec = dockers.load(open(spec_file, 'r'))
        self.langs = ['curl'] + langs
        self.execute_langs = execute_langs

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
        return balanced.Marketplace.find(self.storage['marketplace_uri'])

    @property
    def card(self):
        return balanced.Card.find(self.storage['card_uri'])

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
        self.method = filter(lambda x: x != 'HEAD', match['methods'])[0]
        self.uri = match['path']

    @classmethod
    def qualify_uri(cls, ctx, uri, **qs):
        url = ctx.storage['api_location'] + uri
        if qs:
            url += '?' + urllib.urlencode(qs)
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
            raise ValueError('Multiple endpoints matching "{0}"'.format(name))
        if select == 'any':
            return matches[0]
        elif select == 'shortest':
            return min(matches, key=lambda m: len(m['path']))
        raise ValueError('Unsuported policy "{0}"'.format(select))


class Scenario(object):

    @classmethod
    def bootstrap(cls, ctx):
        # api conf
        if  ctx.storage.get('api_location') != ctx.api_location:
            ctx.storage.clear()
            ctx.storage['api_location'] = ctx.api_location
        balanced.config.root_uri = ctx.storage['api_location']
        if 'api_key' not in ctx.storage:
            ctx.storage.clear()
            ctx.storage['api_location'] = ctx.api_location
            logger.debug('creating api key')
            key = balanced.APIKey().save()
            ctx.storage['api_key'] = key.secret
        balanced.configure(ctx.storage['api_key'])

        # marketplace
        if 'marketplace_id' not in ctx.storage:
            logger.debug('creating marketplace')
            marketplace = balanced.Marketplace().save()
            ctx.storage['marketplace_uri'] = marketplace.uri
            ctx.storage['marketplace_id'] = marketplace.id

        # card
        if 'card_id' not in ctx.storage:
            logger.debug('creating card')
            card = ctx.marketplace.create_card(**{
                'name': 'Benny Riemann',
                'card_number': '4111111111111111',
                'expiration_month': 4,
                'expiration_year': 2014,
                'security_code': 323,
                'street_address': '167 West 74th Street',
                'postal_code': '10023',
                'country_code': 'USA',
                'phone_number': '+16509241212'
            })
            ctx.marketplace.create_buyer(None, card.uri)
            ctx.storage['card_uri'] = card.uri
            ctx.storage['card_id'] = card.id

        # escrow
        thresh_h, thresh_l = 10000000, 100000
        if ctx.marketplace.in_escrow < thresh_l:
            amount = thresh_h - ctx.marketplace.in_escrow
            logger.debug('incrementing escrow balanced %s', amount)
            ctx.card.debit(amount)

    def __init__(self, ctx, path):
        self.ctx = ctx
        self.name = os.path.basename(path)
        self.path = path
        self.definition = None
        self.request = None

    @property
    def metadata(self):
        context = {
            'json': json,
            'ctx': self.ctx,
            'storage': self.ctx.storage,
            'marketplace': self.ctx.marketplace,
        }
        metadata = os.path.join(self.path, 'metadata.py')
        execfile(metadata, context, context)
        return context['request']

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
        block = self._render(template_path)
        block['lang'] = lang
        if block['lang'] == 'curl':
            if 'delete' in self.name:
                logger.info('skipping execution for "%s" (%s)', self.name, block['lang'])
            else:
                block['response'] = json.dumps(
                    json.loads(self._exec_cmd(block['request'])),
                    indent=4,
                    sort_keys=True,
                )
                self.ctx.storage[self.name]['response'] = block['response']
        elif block['lang'] in self.ctx.execute_langs:
            if 'delete' in self.name:
                logger.info('skipping execution for "%s" (%s)', self.name, block['lang'])
            else:
                self._exec_code(block['request'])
        self.ctx.storage[self.name][lang] = block.copy()
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

        # definition
        logger.debug('rendering defintion for "%s"', template_path)
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
        context.update(request=self.metadata)
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

        return {
            'defintion': definition,
            'request': request,
        }

    def _exec_cmd(self, cmd):
        cmd = filter(
            lambda x: x != '\n',
            shlex.split(cmd.encode('utf-8'))
        )
        sh_cmd = ' '.join(pipes.quote(p) for p in cmd)
        logger.debug('exeuting - %s', sh_cmd)
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

    def _exec_code(self, code):
        # TODO: remote code exec
        logger.info('dont work yet')


def generate(write, name, blocks, response, section_chars):
    pygments = {
        'curl': 'bash',
    }

    write('.. cssclass:: {0}\n\n'.format('code-block'))
    write('.. container:: {0}\n\n'.format(name))

    write('defintion\n')
    write('{0}\n'.format(section_chars[0] * len('defintion')))
    write('\n')
    for block in blocks:
        pygment = pygments.get(block['lang'], block['lang'])
        write('.. code:: {0}\n\n'.format(pygment))
        with write:
            write(block['defintion'])
            write('\n')

    write('request\n')
    write('{0}\n'.format(section_chars[0] * len('request')))
    write('\n')
    for block in blocks:
        pygment = pygments.get(block['lang'], block['lang'])
        write('.. code:: {0}\n\n'.format(pygment))
        with write:
            write(block['request'])
            write('\n')

    if response:
        write('response\n')
        write('{0}\n'.format(section_chars[0] * len('response')))
        write('\n')
        write('.. code:: {0}\n\n'.format('javascript'))
        with write:
            write(response)
            write('\n')


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
        default='./scenario.json',
        help='Storage FILE location',
    )
    parser.add_argument(
        '-d', '--directory',
        metavar='DIRECTORY',
        default='./scenarios',
        help='DIRECTORY containing named scenarios',
    )
    parser.add_argument(
        '-p', '--spec',
        metavar='FILE',
        default='../balanced.json',
        help='FILE containing spec data',
    )
    parser.add_argument(
        '--lang',
        metavar='LANGUAGE',
        dest='langs',
        action='append',
        default=[],
        choices=['php', 'python', 'ruby'],
        help='Enable LANGUAGE for the scenario',
    )
    parser.add_argument(
        '-x', '--exec-lang',
        dest='execute_langs',
        metavar='LANGUAGE',
        action='append',
        default=[],
        choices=['php', 'python', 'ruby'],
        help='Execute LANGUAGE for the scenario',
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
        api_location=args.api_location,
        scenarios_dir=args.directory,
        storage_file=args.storage,
        spec_file=args.spec,
        langs=args.langs,
        execute_langs=args.execute_langs,
    )
    Scenario.bootstrap(ctx)
    write = BlockWriter(sys.stdout)
    for scenario in args.scenarios:
        logger.debug('scenario "%s"', scenario)
        scenario = ctx.lookup_scenario(scenario)
        blocks, response = scenario()
        generate(write, scenario.name, blocks, response, args.sections)
    ctx.storage.save()

if __name__ == '__main__':
    main()
