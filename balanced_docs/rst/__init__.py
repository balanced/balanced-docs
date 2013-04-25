import re


class BulletListParser(object):

    def __init__(self):
        self.bullets = []
        self.bullet = []
        self.indent = None
        self._consume = self._consume_start

    def __call__(self, line):
        self._consume(line)

    def done(self):
        self.bullets.append(self.bullet)
        self.bullet = []

    def _consume_start(self, line):
        m = re.match(r'(?P<indent>\s*?)\- ', line)
        if not m:
            raise Exception('Unable to parse bullet list start "{}"'.format(
                line))
        self.indent = len(m.group('indent'))
        self.bullet.append(line[m.end():])
        self._consume = self._comsume_next

    def _comsume_next(self, line):
        m = re.match(r'(?P<indent>\s*?)- ', line)
        if not m:
            if not line.strip():
                self.bullet.append(line)
            else:
                self.bullet.append(line[self.indent + 2:])
        elif len(m.group('indent')) != self.indent:
            self.bullets.append(self.bullet)
        else:
            self.bullets.append(self.bullet)
            self.bullet = []
            self._consume_start(line)

    @classmethod
    def for_block(cls, block):
        p = cls()
        for l in block.split('\n'):
            p(l)
        p.done()
        return p.bullets


class DirectiveParser(object):

    def __init__(self, name, has_content, generator):
        self.name = name
        self.has_content = has_content
        self.generator = generator
        self.args = []
        self.opts = {}
        self.opt_continue = None
        self.content = []
        self.done = False
        self.trailer = None
        self.indent = None
        self._consume = self._consume_header

    @classmethod
    def probe(cls, line):
        match = re.match(cls._header_re, line)
        if not match:
            return None
        return match.group('name')

    def __call__(self, line):
        self._consume(line)

    def render(self):
        indent = ' ' * self.indent
        if not self.has_content and self.content:
            raise ValueError('Directive {} does not support content'.format(self.name))
        if self.has_content:
            for l in self.generator(self.args, self.opts, self.content):
                yield indent + l
        else:
            for l in self.generator(self.args, self.opts):
                yield indent + l

    _header_re = r'(?P<indent>\s*?)\.\.\s+?(?P<name>.+?)::(\s(?P<arg>.+))?'

    _option_re = r'\s*?:(?P<name>.+?):(\s+?(?P<value>.+))?'

    def _consume_header(self, line):
        m = re.match(self._header_re, line)
        if not m:
            raise ValueError('Invalid {} directive header'.format(
                self.name))
        name = m.group('name')
        if self.name != name:
            raise ValueError('Wrong {} directive header'.format(self.name))
        if m.group('arg'):
            self.args += m.group('arg').strip().split()
        self.indent = self._indent(line)
        self._consume = self._consume_block_option

    def _consume_block_option(self, line):
        if not line.strip():
            self._consume = self._consume_block_content
            return
        if self._indent(line) <= self.indent:
            self._done(line)
            return
        m = re.match(self._option_re, line)
        if m:
            if m.group('value') is None:
                self.opts[m.group('name')] = None
            else:
                self.opts[m.group('name')] = m.group('value').strip()
            self.opt_continue = (m.group('name'), m.start('value'))
        else:
            if (self.opt_continue is not None and
                    len(line) - len(line.lstrip()) == self.opt_continue[1]):
                self.opts[self.opt_continue[0]] += ' ' + line.strip()
            else:
                self.opt_continue = None
                self.args.append(line.strip())

    def _consume_block_content(self, line):
        if line.strip():
            indent = self._indent(line)
            if indent <= self.indent:
                self._done(line)
                return
        if self.content or line[self.indent + 3:]:
            self.content.append(line[self.indent + 3:])

    def _consume_done(self, line):
        raise ValueError('Directive {} has been fully parsed'.format(self.name))

    @staticmethod
    def _indent(line):
        return len(line) - len(line.lstrip())

    def _done(self, trailer=None):
        self.done = True
        self.trailer = trailer
        self._consume = self._consume_done


class Overrides(dict):

    SEPARATOR = '.'

    @classmethod
    def load(cls, content):
        parser = BulletListParser()
        for l in content.splitlines():
            parser(l)
        parser.done()
        return Overrides([
            (bullet[0].strip(), '\n'.join(bullet[1:]).strip())
            for bullet in parser.bullets if bullet
        ])

    def has_match(self, path):
        name = self.SEPARATOR.join(path)
        return name in self

    def match(self, path):
        name = self.SEPARATOR.join(path)
        return self[name]


class IncludeExcludeFilter(object):

    def __init__(self, include, exclude):
        self.include = include
        self.exclude = exclude

    def __call__(self, v):
        if self.include:
            include = any(i(v) for i in self.include)
            if not self.exclude:
                return include
            return include and not any(f(v) for f in self.exclude)
        elif self.exclude:
            return not any(f(v) for f in self.exclude)
        return True


class Filter(object):

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
        return self._filter(self.specs, parts[:])

    def _filter(self, specs, parts):
        if not parts:
            return self.missing
        if self.ALL in specs:
            return True
        part = parts.pop(0)
        if part not in specs:
            return False
        specs = specs[part]
        if not specs:
            return True
        return self._filter(specs, parts)


class Context(object):

    def __init__(self, filter, overrides, writer):
        self.filter = filter
        self.overrides = overrides
        self.writer = writer 
        self.path = []

    @property
    def filtered(self):
        return self.filter(self.path)

    @property
    def overriden(self):
        return self.overrides.has_match(self.path)

    @property
    def override(self):
        return self.overrides.match(self.path)

    def __call__(self, name):
        self.push(name)
        return self

    def push(self, name):
        self.path.append(name)

    def pop(self):
        self.path.pop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.pop()


import error
import form
import view
import endpoint
import enum
