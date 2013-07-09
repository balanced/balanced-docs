import json
import re


def load(file_path):
    return Spec(json.load(file_path))


class Spec(dict):

    # endpoints

    @property
    def endpoints(self):
        return self['endpoints']

    def match_endpoint(self, name):
        matches = []
        for endpoint in self.endpoints:
            if name == endpoint['name']:
                matches.append(endpoint)
        return matches

    # views

    @property
    def views(self):
        return self['views']

    def match_view(self, name):

        def _munge(v):
            return re.sub(r'[\_\-\.]', '', v.lower())

        name = _munge(name)
        for view in self.views:
            if name == _munge(view['name']):
                return view
        return None

    # views

    @property
    def forms(self):
        return self['forms']

    def match_form(self, name):

        def _munge(v):
            v = re.sub(r's\.', '.', v)
            return re.sub(r'[\_\-.]', '', v.lower())

        name = _munge(name) + 'form'
        for form in self.forms:
            if name == _munge(form['name']):
                return form
        return None

    # errors

    @property
    def errors(self):
        return self['errors']

    # enums

    @property
    def enums(self):
        return self['enums']

    def match_enum(self, name):

        def _munge(v):
            return re.sub(r'[\_\-\.]', '', v.lower())

        name = _munge(name)
        for enum in self.enums:
            if name == _munge(enum['name']):
                return enum
        return None
