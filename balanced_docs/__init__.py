import argparse
import collections
import functools
import logging
import os
import sys


class BlockWriter(object):

    indent = ' ' * 3

    def __init__(self, io):
        self.io = io
        self._blocks = []

    def __enter__(self):
        self._blocks.append([])
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            for l in ''.join(self._blocks.pop()).split('\n'):
                self(self.indent)
                self(l)
                self('\n')

    def __call__(self, buf):
        if not self._blocks:
            self.io.write(buf)
        else:
            self._blocks[-1].append(buf)


class LogLevelAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        level = getattr(logging, values.upper())
        setattr(namespace, self.dest, level)


class EnvironmentVarAction(argparse.Action):

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

        super(EnvironmentVarAction, self).__init__(
            default=default,
            required=required,
            **kwargs
        )

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


# http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
    '''
    Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
        self.cache[args] = value
        return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


from .rst import DirectiveParser
