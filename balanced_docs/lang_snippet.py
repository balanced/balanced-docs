"""
Backend for the scenario snippet rST directive.

For example:

    .. dcode: scenario
        ...

Maps to:

    def main():
        ...

"""
import os
import sys
import codecs
from os import path

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.util import parselinenos
from sphinx.util.compat import Directive


class LangSnippet(Directive):
    langs = None
    lang_extensions = {
        'curl': 'sh',
        'python': 'py',
        'ruby': 'rb',
        'java': 'java',
        'csharp': 'cs',
        'node': 'js',
        'php': 'php',
    }
    client_dir = None
    rev = 'rev1'
    
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'linenos': directives.flag,
        'lines': directives.unchanged_required,
        'start-after': directives.unchanged_required,
        'end-before': directives.unchanged_required,
    }

    def run(self):
        retnodes = []
        document = self.state.document
        filename = self.arguments[0]

        for lang in self.langs:
            if not document.settings.file_insertion_enabled:
                return [document.reporter.warning('File insertion disabled',
                                                  line=self.lineno)]
            env = document.settings.env

            if lang in ['python', 'ruby', 'php', 'node']:
                fn = os.path.join(self.client_dir, self.rev, lang,
                                             'snippets', filename + '.' + self.lang_extensions[lang])
            if lang == 'curl':
                fn = os.path.join(self.client_dir, self.rev, lang,
                                             'snippets', filename + '.' + self.lang_extensions[lang])
            if lang == 'java':
                fn = os.path.join(self.client_dir, self.rev, lang,
                                             'src', 'snippets',
                                             filename + '.' + self.lang_extensions[lang])
            if lang == 'csharp':
                fn = os.path.join(self.client_dir, self.rev, lang,
                                             'scenarios', 'snippets',
                                             filename + '.' + self.lang_extensions[lang])
            

            encoding = self.options.get('encoding', env.config.source_encoding)
            try:
                f = codecs.open(fn, 'rU')
                lines = f.readlines()
                f.close()
            except (IOError, OSError):
                return [document.reporter.warning(
                    'Include file %r not found or reading it failed' % filename,
                    line=self.lineno)]
            except UnicodeError:
                return [document.reporter.warning(
                    'Encoding %r used for reading included file %r seems to '
                    'be wrong, try giving an :encoding: option' %
                    (encoding, filename))]

            linespec = self.options.get('lines')
            if linespec is not None:
                try:
                    linelist = parselinenos(linespec, len(lines))
                except ValueError, err:
                    return [document.reporter.warning(str(err), line=self.lineno)]
                lines = [lines[i] for i in linelist]

            startafter = self.options.get('start-after')
            endbefore = self.options.get('end-before')
            if startafter is not None or endbefore is not None:
                use = not startafter
                res = []
                for line in lines:
                    if not use and startafter and startafter in line:
                        use = True
                    elif use and endbefore and endbefore in line:
                        use = False
                        break
                    elif use:
                        res.append(line)
                lines = res

            text = ''.join(lines)
            retnode = nodes.literal_block(text, text, source=fn)
            retnode.line = 1
            if lang == 'curl':
                retnode['language'] = 'bash'
            else:
                retnode['language'] = lang
            if 'linenos' in self.options:
                retnode['linenos'] = True
            document.settings.env.note_dependency(fn)
            retnodes.append(retnode)

        return retnodes