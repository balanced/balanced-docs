import json
import re
import os
import sys

import dockers


class Spec(dict):

    def __init__(self, *args, **kwargs):
        self.dockers = kwargs.pop('dockers')
        super(Spec, self).__init__(*args, **kwargs)

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
        return self.dockers.match_enum(name)

    # used on some resources
    # currently not documented in balanced-api
    @property
    def queries(self):
        return self.dockers.queries

    def match_query(self, name):
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

        # if resource == 'card_holds': # and action == 'update':
        #     # TODO asdfasdf, gaaaa
        #     return self.dockers.match_form('holds.' + action)
        # if resource == 'credits':
        #     return self.dockers.match_form(name)

        # action is currently create or update
        #method = 'POST' if action == 'create' else 'PUT'
        if action == 'create':
            reqs = self['resources_create'][resource]
        else:
            reqs = self['resources_update'][resource]
        view = self._find_file('_models/{}.json'.format(resource[:-1]))

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

        def get_type(name):
            disallowed_types = ['null']
            field_types = view['properties'].get(name, {}).get('type')
            if type(field_types) is list:
                for t in field_types:
                    if t not in disallowed_types:
                        return t
            return field_types or 'string'

        return {
            'fields': [
                {
                    'name': name,
                    'description': get_description(name),
                    'nullable': name in nullable,
                    'required': name in required,
                    'tags': [],   # TODO: ?
                    'type': get_type(name), # 'string',  # TODO: this is documented in the 'type' on the properties
                    'validate': None
                } for name in all_keys],
            'type': 'form',
            'name': '{}_{}_form'.format(resource, action)
        }