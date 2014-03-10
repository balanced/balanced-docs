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

        def get_description(view, name):
            try:
                description = view['properties'].get(name, {}).get('description')
            except:
                description = None

            if description is None:
                try:
                    description = (
                        view['properties']
                        .get('links', {}).get('properties', {})
                        .get(name, {}).get('description')
                    )
                except:
                    description = None

            return description

        def get_type(name):
            disallowed_types = ['null']
            field_types = view['properties'].get(name, {}).get('type')
            if type(field_types) is list:
                for t in field_types:
                    if t not in disallowed_types:
                        return t
            return field_types or 'string'


        def generate_form(resource, action):
            fields = []
            for name in all_keys:
                field = {}
                ignored_object_keys = ['links']
                if get_type(name) == 'object':# and name not in ignored_object_keys:
                    resource_model = self._find_file('_models/{}.json'.format(name))
                    subkeys = set()
                    subfields = []

                    for r in reqs:
                        keys = r['request'].keys() if r['request'] else {}
                        if name in r['request']:
                            for key, val in r['request'][name].iteritems():
                                subkeys.add(key)

                    for sk in subkeys:
                        descr = get_description(resource_model, sk)
                        if not descr:
                            continue

                        subfield = {
                            'name': sk,
                            'description': descr,
                            'nullable': sk in nullable,
                            'required': sk in required,
                            'tags': [],
                            'type': get_type(sk),
                            'validate': None
                        }
                        subfields.append(subfield)

                    field = {
                        'form': {
                            'fields': subfields,
                            'type': 'form',
                            'name': '{}_{}_form'.format(name, action),
                            'tags': []
                        },
                        'tags': [],
                        'nullable': name in nullable,
                        'required': name in required,
                        'validate': None,
                        'type': 'form_field' if subfields else 'object',
                        'description': get_description(view, name),
                        'name': name
                    }
                else:
                    field = {
                        'name': name,
                        'description': get_description(view, name),
                        'nullable': name in nullable,
                        'required': name in required,
                        'tags': [],
                        'type': get_type(name),
                        'validate': None
                    }
                fields.append(field)

            return {
                'fields': fields,
                'type': 'form',
                'name': '{}_{}_form'.format(resource, action)
            }

        return generate_form(resource, action)
