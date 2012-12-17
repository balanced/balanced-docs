import sys


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


class _IOWriter(_Writer):

    def __init__(self, io=sys.stdout):
        super(_IOWriter, self).__init__()
        self.io = io

    def line(self, *args):
        self.io.write(self._indentation + ' '.join(map(str, args)))
        self.io.write('\n')
        self._fragment = False

    def fragment(self, *args):
        self.io.write(self._indentation + ' '.join(map(str, args)))
        self._fragment = True


class LineWriter(_Writer):
    def __init__(self, lines):
        super(LineWriter, self).__init__()
        self.lines = lines
        self.buffer = ''

    def line(self, *args):
        line = ''
        if self.buffer:
            line += self.buffer
            self.buffer = ''
        line += self._indentation + ' '.join(map(str, args))
        self.lines.append(line if line.strip() else '')
        self._fragment = False

    def fragment(self, *args):
        fragment = self._indentation + ' '.join(map(str, args))
        self.buffer += fragment
        self._fragment = True


class ViewWriter(_Writer):
    def __init__(self, view):
        super(ViewWriter, self).__init__()
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
