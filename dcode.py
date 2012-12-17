"""
Dynamically generates:

{section}

.. code: {type}
    {content}

blocks from:

.. dcode: {name}
    {options}

"""
from collections import OrderedDict
import json
import os
import string
import shlex
import subprocess
import sys

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from docutils.statemachine import ViewList

from util import LineWriter as _LineWriter, ViewWriter as _ViewWriter


# internals

class _FieldFilter(object):

    SEPARATOR = '.'
    ALL = '*'

    def __init__(self, fields, missing):
        self.specs = {}
        self.missing = missing
        for f in fields:
            specs = self.specs
            for part in f.split(self.SEPARATOR):
                if part not in specs:
                    specs[part] = {}
                specs = specs[part]

    def __call__(self, parts):
        return self._filter(self.specs, map(string.lower, parts))

    def _filter(self, spec, parts):
        if not parts:
            return self.missing
        if self.ALL in spec:
            return True
        part = parts.pop(0).lower()
        if part not in spec:
            return False
        spec = spec[part]
        if not spec:
            return True
        return self._filter(spec, parts)


class _IncludeExcludeFieldFilter(object):

    def __init__(self, include, exclude):
        self.include = include
        self.exclude = exclude

    def __call__(self, parts):
        if self.include:
            include = self.include(parts)
            if not self.exclude:
                return include
            return include and not self.exclude(parts)
        elif self.exclude:
            return not self.exclude(parts)
        return True


class _Formatter(object):

    def __init__(
            self,
            writer,
            sections, section_chars, section_depth,
            directive):
        self.writer = writer
        self.sections = sections
        self.section_chars = section_chars
        self.section_depth = section_depth
        self.directive = directive
        self.path = []

    @property
    def _depth(self):
        return len(self.path)

    def begin_block(self, name):
        self.path.append(name)
        if self._depth < self.section_depth:
            return
        if self.sections:
            self.writer.line(name)
            section_char = self.section_chars[self._depth - self.section_depth]
            self.writer.line(section_char * len(name))
        self.writer.line('.. cssclass:: {}'.format('code-block'))
        self.writer.line()
        self.writer.line('.. container:: {}'.format(name))
        self.writer.indent()
        self.writer.line()

    def end_block(self):
        self.writer.outdent()
        self.path.pop()

    def begin_code(self, type=None):
        self.writer.line('.. {}:: {}'.format(self.directive, (type or '')))
        self.writer.indent()
        self.writer.line()

    def code(self, content):
        for l in content.splitlines():
            self.writer.line(l)

    def end_code(self):
        self.writer.line()
        self.writer.outdent()


class _SpecFormatter(object):

    def __init__(
            self,
            writer,
            sections, section_chars, section_depth,
            directive):
        self.writer = writer
        self.sections = sections
        self.section_chars = section_chars
        self.section_depth = section_depth
        self.directive = directive
        self.path = []

    @property
    def _depth(self):
        return len(self.path)

    def begin_block(self, name):
        self.path.append(name)
        if self._depth < self.section_depth:
            return

        self.writer.line(name)
        section_char = self.section_chars[self._depth - self.section_depth]
        self.writer.line(section_char * len(name))
        self.writer.line()

    def end_block(self):
        self.path.pop()

    def begin_code(self, type=None):
        self.writer.line('.. {}:: {}'.format(self.directive, (type or '')))
        self.writer.indent()
        self.writer.line()

    def code(self, content):
        for l in content.splitlines():
            self.writer.line(l)

    def end_code(self):
        self.writer.line()
        self.writer.outdent()


def _is_leaf(block):
    return not any(
        isinstance(v, (OrderedDict, dict)) for v in block.itervalues()
    )


def _traverse(path, block, filter, formatter):
    if _is_leaf(block):
        if block['content']:
            formatter.begin_code(block.get('type'))
            formatter.code(block['content'])
            formatter.end_code()
    else:
        for k, v in block.iteritems():
            path.append(k)
            if not filter(path):
                path.pop()
                continue
            formatter.begin_block(k)
            _traverse(path, v, filter, formatter)
            formatter.end_block()
            path.pop()


def _execute(script, name):
    args = shlex.split(script.encode('utf-8')) + [name]
    try:
        output = subprocess.check_output(args)
    except subprocess.CalledProcessError, ex:
        print >>sys.stderr, ex.cmd, ' ended with code ', ex.returncode
        print >>sys.stderr, 'Output: \r\n', ex.output
        raise
    blocks = json.loads(output, object_pairs_hook=OrderedDict)
    return blocks


_BLOCK_CACHE = {
}

_BLOCK_CACHE_KEY_FMT = '{script}:{name}'


def _generate(
        script, name,
        includes, excludes,
        sections, section_chars, section_depth,
        cache,
        directive,
        record,
        writer):

    if cache:
        key = _BLOCK_CACHE_KEY_FMT.format(script=script, name=name)
        if key not in _BLOCK_CACHE:
            _BLOCK_CACHE[key] = _execute(script, name)
        blocks = _BLOCK_CACHE[key]
    else:
        blocks = _execute(script, name)
    filter = _IncludeExcludeFieldFilter(
        include=_FieldFilter(includes, True) if includes else None,
        exclude=_FieldFilter(excludes, False) if excludes else None,
    )
    for block in sorted(blocks, key=lambda x: 'response' in x):
        formatter = _Formatter(
            writer,
            sections, section_chars, section_depth,
            directive
        )
        _traverse([], block, filter, formatter)
    if record:
        with open(record, 'a') as fo:
            fo.write(name + '\n')


def _spec_generate(
        script, name,
        includes, excludes,
        sections, section_chars, section_depth,
        cache,
        directive,
        record,
        writer):

    if cache:
        key = _BLOCK_CACHE_KEY_FMT.format(script=script, name=name)
        if key not in _BLOCK_CACHE:
            _BLOCK_CACHE[key] = _execute(script, name)
        blocks = _BLOCK_CACHE[key]
    else:
        blocks = _execute(script, name)

    filter = _IncludeExcludeFieldFilter(
        include=_FieldFilter(includes, True) if includes else None,
        exclude=_FieldFilter(excludes, False) if excludes else None,
    )

    for block in blocks:
        formatter = _SpecFormatter(
            writer,
            sections, section_chars, section_depth,
            directive
        )
        _traverse([], block, filter, formatter)
    if record:
        with open(record, 'a') as fo:
            fo.write(name + '\n')


def run(args, opts, content):
    # arguments
    if len(args) != 1:
        raise ValueError('Requires exactly one argument')
    name = args[0]

    # options
    invalid_opts = set(opts.keys()) - set(DCodeDirective.option_spec.keys())
    if invalid_opts:
        raise ValueError('Unsupported option(s) {}'.format(
            ', '.join(invalid_opts)))
    if 'includes' in opts:
        includes = opts['includes'].split(' ')
    else:
        includes = None
    if 'excludes' in opts:
        excludes = opts['excludes'].split(' ')
    else:
        excludes = None
    if 'section-depth' in opts:
        section_depth = int(opts['section-depth'])
    else:
        section_depth = None
    if 'section-chars' in opts:
        section_chars = opts['section-chars']
    else:
        section_chars = '~' * 10
    if 'script' in opts:
        script = opts['script']
    else:
        script = DCodeDefaultDirective.script

    if 'nospec' in opts:
        spec = False
    else:
        spec = DCodeDefaultDirective.spec

    sections = False if 'no-sections' in opts else True
    cached = True if 'cached' in opts else False

    # content
    if content:
        raise ValueError('Content is not allowed')

    # generate
    lines = []

    func = _generate
    if spec:
        func = _spec_generate

    func(
        script, name,
        includes, excludes,
        sections, section_chars, section_depth,
        cached,
        'code',
        None,
        _LineWriter(lines),
    )

    return lines


class DCodeDefaultDirective(Directive):

    name = 'dcode-default'

    required_arguments = 0

    optional_arguments = 0

    option_spec = {
        'includes': directives.unchanged,
        'excludes': directives.unchanged,
        'no-sections': directives.flag,
        'section-chars': directives.unchanged,
        'section-depth': int,
        'script': directives.unchanged,
        'directive': directives.unchanged,
        'cache': directives.flag,
        'record': directives.unchanged,
        'nospec': directives.unchanged,
    }

    has_content = False

    includes = None
    excludes = None
    sections = False
    sections = True
    section_chars = '~' * 10
    section_depth = 1
    script = 'dcoder'
    directive = 'code'
    cached = False
    record = None
    spec = True

    def run(self):
        cls = type(self)

        # args and opts
        if 'includes' in self.options:
            cls.includes = self.options['includes'].split(' ')
        if 'excludes' in self.options:
            cls.excludes = self.options['excludes'].split(' ')
        if 'no-sections' in self.options:
            cls.sections = False
        if 'section-chars' in self.options:
            cls.section_chars = self.options['section-chars']
        if 'section-depth' in self.options:
            cls.section_depth = self.options['section-depth']
        if 'directive' in self.options:
            cls.directive = self.options['directive']
        if 'script' in self.options:
            cls.script = self.options['script']
        if 'cached' in self.options:
            cls.cached = True
        if 'record' in self.options:
            cls.record = os.path.expanduser(self.options['record'])
        if 'nospec' in self.options:
            cls.spec = False

        # parse
        node = nodes.section()
        node.document = self.state.document
        return node.children

    @classmethod
    def set(cls, args, options, contents):

        # args and opts
        if 'includes' in options:
            cls.includes = options['includes'].split(' ')
        if 'excludes' in options:
            cls.excludes = options['excludes'].split(' ')
        if 'no-sections' in options:
            cls.sections = False
        if 'section-chars' in options:
            cls.section_chars = options['section-chars']
        if 'section-depth' in options:
            cls.section_depth = options['section-depth']
        if 'directive' in options:
            cls.directive = options['directive']
        if 'script' in options:
            cls.script = options['script']
        if 'cached' in options:
            cls.cached = True
        if 'record' in options:
            cls.record = os.path.expanduser(options['record'])
        if 'nospec' in options:
            cls.spec = False


        return []


class DCodeDirective(Directive):

    name = 'dcode'

    required_arguments = 1

    optional_arguments = 4

    option_spec = {
        'includes': directives.unchanged,
        'excludes': directives.unchanged,
        'cache': directives.flag,
        'section-chars': directives.unchanged,
        'section-depth': int,
        'script': directives.unchanged,
        'directive': directives.unchanged,
        'record': directives.flag,
        'no-sections': directives.flag,
        'nospec': directives.unchanged,
    }

    has_content = False

    def run(self):
        # args and opts
        name = self.arguments[0]
        if 'includes' in self.options:
            includes = self.options['includes'].split(' ')
        else:
            includes = DCodeDefaultDirective.includes
        if 'excludes' in self.options:
            excludes = self.options['excludes'].split(' ')
        else:
            excludes = DCodeDefaultDirective.excludes
        if 'no-sections' in self.options:
            sections = False
        else:
            sections = DCodeDefaultDirective.sections
        if 'section-chars' in self.options:
            section_chars = self.options['section-chars']
        else:
            section_chars = DCodeDefaultDirective.section_chars
        if 'section-depth' in self.options:
            section_depth = self.options['section-depth']
        else:
            section_depth = DCodeDefaultDirective.section_depth
        if 'directive' in self.options:
            directive = self.options['directive']
        else:
            directive = DCodeDefaultDirective.directive
        if 'script' in self.options:
            script = self.options['script']
        else:
            script = DCodeDefaultDirective.script
        if 'cached' in self.options:
            cached = True
        else:
            cached = DCodeDefaultDirective.cached
        if 'record' in self.options:
            record = os.path.expanduser(self.options['record'])
        else:
            record = DCodeDefaultDirective.record
        if 'nospec' in self.options:
            spec = False
        else:
            spec = DCodeDefaultDirective.spec


        # generate
        writer = _ViewWriter(ViewList())

        func = _generate
        if spec:
            func = _spec_generate

        func(
            script, name,
            includes, excludes,
            sections, section_chars, section_depth,
            cached,
            directive,
            record,
            writer,
        )

        # parse
        node = nodes.section()
        node.document = self.state.document
        self.state.nested_parse(writer.view, 0, node, match_titles=1)
        return node.children


# test

if __name__ == '__main__':
    for l in run(['credits-update'],
                 {'includes': 'response.*',
                  'section-depth': 2,
                  'cache': True,
                  },
                 None):
        print l
