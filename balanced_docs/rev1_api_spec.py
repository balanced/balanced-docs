# this file for parsing the data in the https://github.com/balanced/balanced-api
# repo to generate the necessary data for the specs

import json
import re
import os
import sys

import dockers

def find_file(fromFile, fileName):
    path = os.path.join(os.path.dirname(fromFile), fileName)
    if os.path.isfile(path):
        return path
    path = os.path.join('..', fileName)
    if os.path.isfile(path):
        return path
    import ipdb; ipdb.set_trace()
    sys.stderr.write('Could not find file {0}\n'.format(fileName))
    sys.exit(1)

def resolve_refs(contents, fileName):
    if isinstance(contents, dict):
        if '$ref' in contents:
            path = find_file(fileName, contents['$ref'])
            cont = open(path).read()
            contents.pop('$ref')
            return resolve_refs(dict(json.loads(cont).items() + contents.items()), path)
        else:
            return dict(
                (k, resolve_refs(v, fileName))
                for k, v in contents.iteritems()
            )
    elif isinstance(contents, list):
        return [resolve_refs(v, fileName) for v in contents]
    else:
        return contents


class Spec(object):

    def __init__(self, path, dockers):
        self.path = path
        self.dockers = dockers

    @property
    def raw_json(self):
        ret = {}
        for (directory, _, files) in os.walk(self.path):
            for f in files:
                if f.endswith('.json'):
                    path = os.path.join(directory, f)
                    ret[path] = resolve_refs(json.load(open(path)), path)
        return ret

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
        import ipdb; ipdb.set_trace()
        print('Getting enum: ', name)
        return self.dockers.match_enum(name)

    # used on some resources
    # currently not documented in balanced-api
    @property
    def queries(self):
        return self.dockers.queries

    def match_query(self, name):
        import ipdb; ipdb.set_trace()
        print('Getting query: ', name)
        return self.dockers.match_query(name)

    # this is the big one, lots of
    # @property
    # def forms(self):
    #     return self.dockers.forms

    def match_form(self, name):
        resource, action = name.split('.')
        relevant = []
        for k, v in self.raw_json.iteritems():
            if k.endswith('{}.json'.format(resource)):
                relevant.append(v)
        return relevant
        print('Getting from: ', name)
        return self.dockers.match_form(name)
