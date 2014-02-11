# this file for parsing the data in the https://github.com/balanced/balanced-api
# repo to generate the necessary data for the specs

import json
import re
import os
import sys

import dockers


class Spec(dict):

    def __init__(self, *args, **kwargs):
        self.dockers = kwargs.pop('dockers')
        super(Spec, self).__init__(*args, **kwargs)

    # @property
    # def raw_json(self):
    #     ret = {}
    #     for (directory, _, files) in os.walk(self.path):
    #         for f in files:
    #             if f.endswith('.json'):
    #                 path = os.path.join(directory, f)
    #                 ret[path] = resolve_refs(json.load(open(path)), path)
    #     return ret

    def _find_file(self, name):
        for n, schema in self['schemas'].iteritems():
            if name in n:
                return schema
        return {}

    # endpoint is currently unused
    @property
    def endpoints(self):
        return self.dockers.endpoints

    def match_endpoint(self, name):
        return self.dockers.match_endpoint(name)

    # errors is currently unused
    @property
    def errors(self):
        return self.dockers.errors

    # views is unused in rev1
    @property
    def views(self):
        return self.dockers.view

    def match_view(self, name):
        print('Getting view: ', name)
        return self.dockers.match_view(name)

    # only used for audit events
    @property
    def enums(self):
        return self.dockers.enums

    def match_enum(self, name):
        #import ipdb; ipdb.set_trace()
        #print('Getting enum: ', name)
        return self.dockers.match_enum(name)

    # used on some resources
    # currently not documented in balanced-api
    @property
    def queries(self):
        return self.dockers.queries

    def match_query(self, name):
        #import ipdb; ipdb.set_trace()
        #print('Getting query: ', name)
        return self.dockers.match_query(name)

    # this is the big one, lots of
    # @property
    # def forms(self):
    #     return self.dockers.forms

    def match_form(self, name):
        resource, action = name.split('.')

        # HAX, holds is coming in from somewhere
        resource = {
            'holds': 'card_holds'
        }.get(resource, resource)

        if resource == 'card_holds' and action == 'update':
            # TODO asdfasdf
            return self.dockers.match_form('holds.update')

        # action is currently create or update
        #method = 'POST' if action == 'create' else 'PUT'
        if action == 'create':
            reqs = self['resources_create'][resource]
        else:
            reqs = self['resources_update'][resource]
        view = self._find_file('_models/{}.json'.format(resource[:-1]))

        #import ipdb; ipdb.set_trace()
        # keys will only be required on create
        required = set(reqs[0]['request'].keys() if reqs[0]['request'] else {})
        all_keys = set(required)  # make a copy of the inital set
        nullable = set()
        for r in reqs:
            keys = r['request'].keys() if r['request'] else {}
            # if the key is in all requests then it is required
            required = required.intersection(keys)
            # basically merge the names of all the keys
            all_keys.update(keys)
            if r['request']:
                for key, val in r['request'].iteritems():
                    if val is None:
                        nullable.add(key)
        # for key, val in view['properties'].iteritems():
        #     if

        # description = view['properties'].get(name, {}).get('description')
        # if not description:
        #     description = view['properties'].get('links', {}).get(name, {}).get('description')


        def get_description(name):
            try:
                return (
                    view['properties'].get(name, {}).get('description') or
                    view['properties'].get('links', {}).get(name, {}).get('description')
                )
            except:
                print name
                print resource
                print action
                print view
                raise
            # TODO: also get the description off the top level links descriptions

        return {
            'fields': [
                {
                    'name': name,
                    'description': get_description(name),
                    'nullable': name in nullable,
                    'required': name in required,
                    'tags': [],   # TODO: ?
                    'type': 'string',  # TODO: this is documented in the 'type' on the properties
                    'validate': None
                } for name in all_keys],
            'type': 'form',
            'name': '{}_{}_form'.format(resource, action)
        }


        # relevant = []
        # for k, v in self.raw_json.iteritems():
        #     if k.endswith('{}.json'.format(resource)):
        #         relevant.append(v)
        # return relevant
        # print('Getting from: ', name)
        # return self.dockers.match_form(name)



# reference for what the output for the forms looks like
reference = \
            {u'fields': [{u'default': u'If the resolving URI references a hold then the default ``amount``\nis the ``amount`` associated with that hold. Otherwise no default\nis provided and this field is **required**.',
   u'description': u'If the resolving URI references a hold then this is hold amount. You can\nalways capture less than the hold amount (e.g. a partial capture).\nOtherwise its the maximum per debit amount for your marketplace.',
   u'name': u'amount',
   u'nullable': False,
   u'required': False,
   u'tags': [],
   u'type': u'integer',
   u'validate': None},
  {u'description': u'Text that will appear on the buyer\'s statement. Characters that can be\nused are limited to:\n\n- ASCII letters (``a-z`` and ``A-Z``)\n- Digits (``0-9``)\n- Special characters (``.<>(){}[]+&!$;-%_?:#@~=\'" ^\\`|``)\n\nAny other characters will be rejected.\n\nDebits - Truncated to 18 characters.\nCredits - Truncated to 14 characters.\n\nAll Visa, Master Card, Discover, American Express debits will have a prefix of "BAL*"\ne.g. "BAL*marketplace.com".\n\nACH debits and credits do not have a prefix.\n\nAmerican Express pending transactions will be shown as "BALANCED INC". AMEX\npending transactions are hidden by default in the American Express web portal.\nOnce the debit is settled it will convert to "BAL*<appears_on_statement_as>".',
   u'name': u'appears_on_statement_as',
   u'nullable': False,
   u'required': False,
   u'tags': [],
   u'type': u'string',
   u'validate': None},
  {u'default': {},
   u'description': u'Single level mapping from string keys to string values.',
   u'name': u'meta',
   u'nullable': False,
   u'required': False,
   u'tags': [],
   u'type': u'key-value',
   u'validate': None},
  {u'default': None,
   u'description': None,
   u'name': u'description',
   u'nullable': False,
   u'required': False,
   u'tags': [],
   u'type': u'string',
   u'validate': None},
  {u'description': None,
   u'name': u'order',
   u'nullable': False,
   u'required': False,
   u'tags': [],
   u'type': u'string',
   u'validate': None}],
 u'name': u'DebitCreateForm',
 u'type': u'form'}
