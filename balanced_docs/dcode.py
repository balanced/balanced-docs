"""
Generates rST by via external scripts.

Use the `dcode-default` directive to set default options:

.. dcode-default: [key]
    :cache: true
    :record: /tmp/dcode.track
    :script: some-script
    :{script-option-1}:
    ...
    :{script-option-n}:

And the `dcode` directive to capture generated rST:

.. dcode: [{key}] [{script-arg-1}] .. [{script-arg-n}]
    :{script-option-1}: value(s)
    ...
    :{script-option-n}: value(s)

    {content}

Note that default options can be overridden by `dcode`.
"""
from collections import defaultdict
import logging
import os
import pipes
import shlex
import subprocess
import sys

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from docutils.statemachine import ViewList
from pprint import pprint

logger = logging.getLogger(__name__)


class DCodeDefaultDirective(Directive):

    class Registry(dict):

        def __init__(self):
            super(DCodeDefaultDirective.Registry, self).__init__(
                script=None,
                cache=False,
                record=None,
                ignore=False,
            )

    registry = defaultdict(Registry)

    @classmethod
    def expand(cls, args, options):
        if args:
            key = args[0]
        else:
            key = None
        if 'cache' in options:
            cls.registry[key]['cache'] = True
        if 'script' in options:
            cls.registry[key]['script'] = options['script']
        if 'record' in options:
            cls.registry[key]['record'] = os.path.expanduser(options['record'])
        if 'ignore' in options:
            cls.registry[key]['ignore'] = True
        return []

    # Directive

    name = 'dcode-default'

    required_arguments = 0

    optional_arguments = 1

    option_spec = {
        'script': directives.unchanged,
        'cache': directives.flag,
        'ignore': directives.flag,
        'record': directives.unchanged,
        'ignore': directives.unchanged,
    }

    has_content = False

    def run(self):
        self.expand(self.arguments, self.options)
        node = nodes.section()
        node.document = self.state.document
        return node.children


class DCodeDirective(Directive):

    @classmethod
    def expand(cls, arguments, options, content):
        # key, args
        if arguments and arguments[0] in DCodeDefaultDirective.registry:
            key = arguments[0]
            args = arguments[1:]
        else:
            key = None
            args = arguments[:]

        # cache
        if 'cache' in options:
            cache = True
        else:
            cache = DCodeDefaultDirective.registry[key]['cache']

        # ignore
        if 'ignore' in options:
            ignore = True
        else:
            ignore = DCodeDefaultDirective.registry[key]['ignore']

        # script
        if 'script' in options:
            script = options['script']
        else:
            script = DCodeDefaultDirective.registry[key]['script']

        # record
        if 'record' in options:
            record = os.path.expanduser(options['record'])
        else:
            record = DCodeDefaultDirective.registry[key]['record']

        # kwargs
        kwargs = dict(
            (k, v.split())
            for k, v in options.iteritems()
            if k not in cls.option_spec
        )

        # generate
        if not script:
            import ipdb; ipdb.set_trace()
        writer = _ViewWriter(ViewList())
        if not ignore:
            if isinstance(content, list):
                content = '\n'.join(content)
            _generate(
                cache=cache,
                record=record,
                writer=writer,
                script=script,
                args=args,
                kwargs=kwargs,
                content=content,
            )
        return writer.view

    # Directive

    name = 'dcode'

    required_arguments = 0

    optional_arguments = 100

    option_spec = {
        'cache': directives.flag,
        'script': directives.unchanged,
        'record': directives.unchanged,
    }

    has_content = True

    def run(self):
        view = run(self.arguments, self.options, self.content)
        node = nodes.section()
        node.document = self.state.document
        self.state.nested_parse(view, 0, node, match_titles=1)
        return node.children


# internals


class _Writer(object):

    def __init__(self):
        self._indent = []
        self._fragment = False

    def __enter__(self):
        self.indent()
        return self

    def __exit__(self, type, value, traceback):
        self.outdent()

    def indent(self, l=4):
        self._indent.append(' ' * l)

    def outdent(self):
        self._indent.pop()

    @property
    def _indentation(self):
        if self._fragment:
            i = ''
        else:
            i = ''.join(self._indent)
        return i

    def line(self, *args):
        raise NotImplementedError()

    def fragment(self, *args):
        raise NotImplementedError()


class _ViewWriter(_Writer):
    def __init__(self, view):
        super(_ViewWriter, self).__init__()
        self.view = view
        self.buffer = ''

    def line(self, *args):
        line = ''
        if self.buffer:
            line += self.buffer
            self.buffer = ''
        line += self._indentation + ' '.join(map(str, args))
        self.view.append(line if line.strip() else '', '<autopilo>')
        self._fragment = False

    def fragment(self, *args):
        fragment = self._indentation + ' '.join(map(str, args))
        self.buffer += fragment
        self._fragment = True


def _execute(script, args, kwargs, content):
    cmd = (
        shlex.split(script.encode('utf-8')) +
        args +
        ['--{}={}'.format(k, v) for k, vs in kwargs.iteritems() for v in vs]
    )
    sh_cmd = ' '.join(pipes.quote(p) for p in cmd)
    logger.debug('executing "%s"', sh_cmd)
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate(content or '')
    if proc.returncode != 0:
        print >>sys.stderr, sh_cmd, '- failed with exit code', proc.returncode
        print >>sys.stderr, 'stderr:'
        print >>sys.stderr, stderr
        print >>sys.stderr, 'stdout:'
        print >>sys.stderr, stdout
        raise Exception('{} - failed with exit code {}'.format(sh_cmd, proc.returncode))
    return stdout


_CACHE = {
}


def _cache_key(script, args, kwargs):
    raise NotImplemented()


def _generate(
        cache,
        record,
        script,
        args,
        kwargs,
        content,
        writer
    ):

    if False and cache:
        key = _cache_key(script, args, kwargs, content)
        if key in _CACHE:
            logger.debug('cache hit "%s"', key)
            result = _CACHE[key]
        else:
            result = _execute(script, args, kwargs, content)
            logger.debug('cache store "%s"', key)
            _CACHE[key] = result
    else:
        result = _execute(script, args, kwargs, content)

    for line in result.splitlines():
        writer.line(line)

    if False and record:
        with open(record, 'a') as fo:
            fo.write(name + '\n')
