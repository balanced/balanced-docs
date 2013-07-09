"""
Generates rST by running external scripts.

Use the `dcode-default` directive to set default options:

.. dcode-default: [{key}]
    :cache: true
    :record: /tmp/dcode.record
    :script: some-script
    :{script-option-1}:
    ...
    :{script-option-n}:

And the `dcode` directive to capture generated rST:

.. dcode: {key} [{script-arg-1}] .. [{script-arg-n}]
    :{script-option-1}: value(s)
    ...
    :{script-option-n}: value(s)

    {content}

Note that default options can be overridden by `dcode`.
"""
from collections import defaultdict
import errno
import functools
import hashlib
import json
import logging
import os
import pipes
import re
import shlex
import subprocess
import sys

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from docutils.statemachine import ViewList

logger = logging.getLogger(__name__)


# internals

class _LangSectionFilter(object):

    def __init__(self, chars, include, write):
        self.section_adornments = chars
        self.writer = write
        self.filtered = False
        self.include = include
        self._filtering_in_progress = False

    def __call__(self, current_line):
        # skip line is a way for the is_section_filtered method to dictate
        # whether or not we should discard the line that we're on.
        #
        # this is because we don't want to output some section headers
        # that are annotating the end of a line or something similar to that
        skip_line = False

        if self._is_section_annotation(current_line):
            is_filtered, skip_line = self._is_section_filtered(current_line)
            if is_filtered:
                return

        if not self._filtering_in_progress and not skip_line:
            self.writer(current_line)

    def _is_section_annotation(self, current_line):
        curr_line = current_line.strip()
        return any([
            curr_line.startswith('.. begin-section:'),
            curr_line.startswith('.. end-section:')
        ])

    def _is_section_filtered(self, current_line):
        is_filtered = False
        skip_line = False

        curr_line = current_line.strip()

        if 'begin-section' in curr_line:
            section_name = curr_line.replace('.. begin-section:', '').strip()
            # if section name is not in our includes, it means its filtered
            is_filtered = (section_name not in self.include)
            skip_line = True
            if is_filtered:
                logger.debug('filtering on for "%s"', section_name)
                self._filtering_in_progress = True

        elif 'end-section' in curr_line:
            section_name = curr_line.replace('.. end-section:', '').strip()
            # reset the section
            logger.debug('finished filtering for "%s"', section_name)
            self._filtering_in_progress = False
            skip_line = True

        return is_filtered, skip_line

    def done(self):
        pass


class _SectionFilter(object):

    INCLUDE_SEPARATOR = '.'

    def __init__(self, chars, include, write):
        self.section_adornments = chars
        self.write = write
        self.filtered = False
        self.include = [
            map(lambda x: x.lower(), i.split(self.INCLUDE_SEPARATOR))
            for i in include
        ]
        self._depth = 0
        self._chars = None
        self._heading = None

    def __call__(self, current_line):
        # if there's a heading set
        if self._heading:
            if self._is_section(self._heading, current_line):
                self._on_section(self._heading, current_line)
            else:
                # write out the heading and the corresponding line
                self._write(self._heading)
                self._write(current_line)
            # reset the header
            self._heading = None
            return
        if current_line and not current_line[0].isspace():
            self._heading = current_line
            return
        # this should really be called "write space"
        self._write(current_line)

    def done(self):
        if self._heading:
            self._write(self._heading)
            self._heading = None

    def _write(self, l):
        if self.filtered:
            self.write(l)

    def _is_section(self, heading, adornment):
        h = heading.rstrip()
        a = adornment.rstrip()
        return (
            a and
            len(a) == len(h) and
            not a[0].isalnum() and
            len(set(a)) == 1
        )

    def _on_section(self, heading, adornment):
        if self.filtered:
            if adornment[0] in self._chars:
                self._write(heading)
                self._write(adornment)
            else:
                logger.debug('filtering off for "%s", "%s"',
                             heading, adornment)
                self.filtered = False
                self._depth = 0
                self._on_section(heading, adornment)
        else:
            if self.section_adornments[self._depth] != adornment[0]:
                self._depth = 0
            else:
                for i in self.include:
                    if len(i) <= self._depth:
                        continue
                    if i[self._depth] == heading.lower():
                        self._depth += 1
                        if len(i) == self._depth:
                            logger.debug('filtering on for "%s", "%s"',
                                         heading, adornment)
                            self._chars = self.section_adornments[self._depth:]
                            self.filtered = True


def _execute(script, args, kwargs, content, record=None):
    args = args[:]
    for k, v in kwargs.iteritems():
        if isinstance(v, list):
            args.extend('--{0}={1}'.format(k, str(vv)) for vv in v)
        elif isinstance(v, bool):
            args.append('--{0}'.format(k))
        else:
            args.append('--{0}={1}'.format(k, str(v)))
    cmd = (
        shlex.split(script.encode('utf-8')) +
        args
    )
    sh_cmd = ' '.join(pipes.quote(p) for p in cmd)
    logger.debug('executing "%s"', sh_cmd)
    if record:
        with open(record, 'a') as fo:
            fo.write(sh_cmd + '\n')
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
        raise Exception('{0} - failed with exit code {1}'.format(sh_cmd, proc.returncode))
    return stdout


class Cache(dict):

    @classmethod
    def key(cls, script, args, kwargs, content):
        m = hashlib.md5()
        m.update(script)
        for arg in sorted(args):
            m.update(arg)
        for k, v in sorted(kwargs.items()):
            m.update(k)
            for vv in v:
                m.update(vv)
        for l in content:
            m.update(l)
        return m.hexdigest()

    @classmethod
    def load(cls, file_path):
        try:
            with open(file_path, 'r') as fo:
                cache = Cache(json.load(fo))
                logger.debug('loaded cache from "%s"', file_path)
        except IOError, ex:
            if ex.errno != errno.ENOENT:
                raise
            logger.debug('no cache @ "%s"', file_path)
            cache = Cache()
        return cache

    def save(self, file_path):
        with open(file_path, 'w') as fo:
            json.dump(self, fo, indent=4)
        logger.debug('saved cache to "%s"', file_path)


def _generate(
        cache_file,
        record,
        script,
        args,
        kwargs,
        content,
        write
    ):
    if cache_file:
        cache = Cache.load(cache_file)
        key = cache.key(script, args, kwargs, content)
        if key in cache:
            logger.debug('cache hit "%s"', key)
            result = cache[key]
        else:
            logger.debug('cache miss "%s"', key)
            result = _execute(script, args, kwargs, content, record)
            logger.debug('cache store "%s"', key)
            cache[key] = result
            cache.save(cache_file)
    else:
        result = _execute(script, args, kwargs, content, record)

    for line in result.splitlines():
        write(line)


_SECTION_FILTER_REGISTRY = {
    'SectionFilter': _SectionFilter,
    'LangSectionFilter': _LangSectionFilter,
}

# exposed


class DCodeDefaultDirective(Directive):

    class Registry(dict):

        def __init__(self, parent, defaults=None):
            self.parent = parent
            super(type(self), self).__init__(defaults or {})

        def __getitem__(self, key):
            try:
                return super(type(self), self).__getitem__(key)
            except KeyError:
                return self.parent[key]

    default_registry = Registry(
        None,
        {'script': None,
         'cache': None,
         'record': None,
         'ignore': False,
         'section-include': None,
         'section-chars': '~^',
         'section-filter-class': _SectionFilter,
         }
    )

    registry = defaultdict(functools.partial(Registry, default_registry))
    registry[None] = default_registry

    @classmethod
    def expand(cls, args, options):
        if args:
            key = args[0]
        else:
            key = None
        if 'cache' in options:
            cls.registry[key]['cache'] = options['cache']
        if 'script' in options:
            cls.registry[key]['script'] = options['script']
        if 'record' in options:
            cls.registry[key]['record'] = os.path.expanduser(options['record'])
        if 'ignore' in options:
            cls.registry[key]['ignore'] = True
        if 'section-chars' in options:
            cls.registry[key]['section-chars'] = options['section-chars']
        if 'section-include' in options:
            cls.registry[key]['section-include'] = options.get(
                'section-include'
            ).split()
        if 'section-filter-class' in options:
            section_filter_class = _SECTION_FILTER_REGISTRY[
                options['section-filter-class']
            ]
            cls.registry[key]['section-filter-class'] = section_filter_class

        kwargs = dict(
            (k, v.split())
            for k, v in options.iteritems()
            if k not in cls.option_spec_fixed
        )
        cls.registry[key].update(kwargs)
        return []

    # Directive

    name = 'dcode-default'

    required_arguments = 0

    optional_arguments = 1

    option_spec = defaultdict(lambda: directives.unchanged)
    option_spec.update({
        'script': directives.unchanged,
        'cache': directives.unchanged,
        'ignore': directives.flag,
        'record': directives.unchanged,
        'ignore': directives.unchanged,
        'section-chars': directives.unchanged,
        'section-include': directives.unchanged,
        'section-filter-class': directives.unchanged,
    })
    option_spec_fixed = option_spec.keys()

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
            cache = options['cache']
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

        # section-*
        if 'section-chars' in options:
            section_chars = options['section-chars']
        else:
            section_chars = DCodeDefaultDirective.registry[key]['section-chars']
        if 'section-include' in options:
            section_include = options['section-include'].split()
        else:
            section_include = DCodeDefaultDirective.registry[key]['section-include']

        if 'section-filter-class' in options:
            section_filter_class = options['section-filter-class']
        else:
            section_filter_class = DCodeDefaultDirective.registry[key].get(
                'section-filter-class',
                'SectionFilter'
            )

        section_filter_class = _SECTION_FILTER_REGISTRY[section_filter_class]

        # kwargs
        excludes = cls.option_spec_fixed + (
            DCodeDefaultDirective.option_spec_fixed
        )
        kwargs = dict(
            (k, v)
            for k, v in DCodeDefaultDirective.registry[key].iteritems()
            if k not in excludes
        )
        kwargs.update(dict(
            (k, v.split())
            for k, v in options.iteritems()
            if k not in excludes
        ))

        # generate
        if not script:
            raise ValueError('No scripts for key "{0}"'.format(key))
        view = ViewList()

        def write(l):
            view.append(l if l.strip() else '', '<dcode>')

        if section_include:
            write = section_filter_class(
                section_chars,
                section_include,
                write,
            )

        if not ignore:
            if isinstance(content, list):
                content = '\n'.join(content)
            _generate(
                cache_file=cache,
                record=record,
                write=write,
                script=script,
                args=args,
                kwargs=kwargs,
                content=content,
            )

        if section_include:
            write.done()

        return view

    # Directive

    name = 'dcode'

    required_arguments = 0

    optional_arguments = 100

    option_spec = defaultdict(lambda: directives.unchanged)
    option_spec.update({
        'cache': directives.flag,
        'script': directives.unchanged,
        'record': directives.unchanged,
        'section-include': directives.unchanged,
        'section-chars': directives.unchanged,
    })
    option_spec_fixed = option_spec.keys()

    has_content = True

    def run(self):
        view = self.expand(
            self.arguments,
            self.options,
            '\n'.join(self.content)
        )
        node = nodes.section()
        node.document = self.state.document
        self.state.nested_parse(view, 0, node, match_titles=1)
        return node.children
