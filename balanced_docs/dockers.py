import json
import re


def load(file_path, rev='rev0'):
    data = json.load(file_path)
    return Spec(data[rev])


class Spec(dict):

    # endpoints

    @property
    def endpoints(self):
        return self['endpoints']

    def match_endpoint(self, name):

        def _nested(path, nesting):
            i = 0
            for part in nesting:
                i = path.find('/' + part, i)
                if i == -1:
                    return False
            return True

        nesting, _, name = name.rpartition('/')
        nesting = nesting.split('/')
        matches = []
        for endpoint in self.endpoints:
            if name == endpoint['name']:
                if nesting and not _nested(endpoint['path'], nesting):
                    continue
                matches.append(endpoint)
        return sorted(matches, key=lambda x: len(x['path']))

    # views

    @property
    def views(self):
        return self['views']

    def match_view(self, name):

        def _munge(v):
            return re.sub(r'[\_\-\.]', '', v.lower())

        name = _munge(name) + 'view'
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
