import argparse
import cPickle as pickle
import os

import balanced
from decorator import decorator
from docutils.parsers.rst import directives
from sphinx.directives import TocTree


class NewTocTree(TocTree):
    option_spec = dict(TocTree.option_spec,
                       reversed=directives.flag)

    def run(self):
        rst = super(NewTocTree, self).run()
        if 'reversed' in self.options:
            rst[0][0]['entries'].reverse()
        return rst


_URL_MAP_FILE = 'urlmap.pickle'
_URL_MAP = pickle.load(open(_URL_MAP_FILE))


def routify(endpoint, exclude_methods=None, all_endpoints=False):
    exclude_methods = exclude_methods or ['HEAD']
    # routes to endpoint(s)
    rules = _URL_MAP[endpoint]

    def iterate_through_rule(the_rules):
        routes = []
        for r in the_rules:
            methods = [m for m in r['methods'] if m not in exclude_methods]
            routes.append([methods[0], r['url']])
        return routes

    endpoints = iterate_through_rule(rules)
    return endpoints[0] if not all_endpoints else endpoints


# encoding

_ERROR_MSG = 'Object of type {0} with value of {1} is not JSON serializable'


class JSONSterlingSerializer(object):

    def __init__(self, explicit_none_check=False):
        self.serialization_chain = []
        self.explicit_none_check = explicit_none_check

    def add(self, callable_serializer):
        self.serialization_chain.append(callable_serializer)
        return self

    def __call__(self, serializable):
        for serializer in self.serialization_chain:
            result = serializer(serializable)
            if ((not self.explicit_none_check and result) or
                (self.explicit_none_check and result is not None)):
                return result

        error_msg = _ERROR_MSG.format(type(serializable), repr(serializable))
        raise TypeError(error_msg)


def handle_datetime(serializable):
    if hasattr(serializable, 'isoformat'):
        # Serialize DateTime objects to RFC3339 protocol.
        # http://www.ietf.org/rfc/rfc3339.txt
        return serializable.isoformat() + 'Z'


def serialize_Resource(serializable):
    if not isinstance(serializable, balanced.Resource):
        return None

    return serializable.__dict__


# should be a singleton
default_json_serializer = JSONSterlingSerializer()
default_json_serializer.add(handle_datetime)
default_json_serializer.add(serialize_Resource)


# xxx

def recursive_expand(dikt, delimiter='\\'):
    if not dikt:
        raise StopIteration

    keys = sorted(dikt.keys(), key=lambda x: isinstance(dikt[x], dict))
    try:
        last = keys[-1]
    except IndexError:
        last = keys[0]

    for k in keys:
        if isinstance(dikt[k], dict):
            for subk, v, slash in recursive_expand(dikt[k], delimiter):
                yield '{}[{}]'.format(k, subk), v, slash
        else:
            yield k, dikt[k], '' if k is last else delimiter


@decorator
def cd_to_path(function, path, *args, **kwargs):
    current_path = os.getcwd()
    os.chdir(path)
    try:
        return function(path, *args, **kwargs)
    finally:
        os.chdir(current_path)


# opts

class EnvDefault(argparse.Action):
    def __init__(self, env_var, required=True, default=None, **kwargs):
        # if we passed in a default and the variable we're looking for
        # is in our environment, it takes precedence over the default
        if default:
            if env_var in os.environ:
                default = os.environ[env_var]
        else:
            default = os.environ.get(env_var)

        if required and default:
            required = False

        super(EnvDefault, self).__init__(
            default=default,
            required=required,
            **kwargs
        )

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)