import sys


class BlockWriter(object):

    indent = ' ' * 4

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


from .rst import DirectiveParser
