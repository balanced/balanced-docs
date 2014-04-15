import json
import re
import os
import sys
from urlparse import urlparse
from collections import defaultdict

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

    @property
    def endpoints(self):
        methods_to_act = {
            'POST': 'create',
            'PUT': 'update',
            'PATCH': 'patch',
            'DELETE': 'delete',
        }
        def _compute_pattern(url):
            path = urlparse(url).path.split('/')
            for x in xrange(1, len(path)):
                if x % 2 == 0:
                    path[x] = ':{}_id'.format(path[x-1][:-1])
            return '/'.join(path)
        results = defaultdict(set)
        for req in self['requests']:
            u = _compute_pattern(req['endpoint'])
            results[u].add(req['method'])
        names = {}
        for k,v  in results.iteritems():
            n = k.split('/')
            if len(n) <= 3:
                # /cards or /cards/CC123123
                resource = n[1]
            elif len(n) >= 4:
                # /customers/:customer_id/orders
                resource = n[3]
            for method in v:
                nn = '{}.{}'.format(resource,
                                    methods_to_act.get(method, 'show'))
                if not names.get(nn) or len(names[nn]['path']) > len(k):
                    names[nn] = {
                        'description': 'TODO:',
                        'methods': list(v),
                        'name': nn,
                        'path': k,
                    }
        return names

    def match_endpoint(self, name):
        resource, act = name.split('.')
        resource = {
            # omg, why
            'bank_account_verifications': 'verifications',
        }.get(resource, resource)
        name = '{}.{}'.format(resource, act)
        g = self.endpoints.get(name)
        if g:
            return [g]
        if act == 'index':
            # the indexs all have the same form in rev1
            return [{
                'description': 'TODO:',
                'methods': ['GET', 'HEAD'],
                'name': name,
                'path': '/{}'.format(name)
            }]
        if act == 'delete':
            # me being lazy, not all resources have a delete example
            act = 'show'
            g = self.endpoints['{}.{}'.format(resource, act)].copy()
            g['methods'] = ['DELETE']
            return [g]
        return []

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

            def fields_sort(a, b):
                if a['required'] and not b['required']:
                    return -1
                if not a['required'] and b['required']:
                    return 1
                return 0

            fields.sort(key=lambda x: x['name'])
            fields.sort(cmp=fields_sort)

            return {
                'fields': fields,
                'type': 'form',
                'name': '{}_{}_form'.format(resource, action)
            }

        return generate_form(resource, action)
