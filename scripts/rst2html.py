#!/usr/bin/env python
"""
A minimal front end to the Docutils Publisher, producing HTML.
"""
try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.parsers.rst import directives

from doxx import pez, pilo, wag, dcode


# TODO: patch docutils to accept --register-directive
directives.register_directive('dcode-default', dcode.DCodeDefaultDirective)
directives.register_directive('dcode', dcode.DCodeDirective)
directives.register_directive('pez', pez.PezDirective)
directives.register_directive('pilo', pilo.PiloDirective)
directives.register_directive('wag-route', wag.WagRouteDirective)

description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

# Command line
publish_cmdline(writer_name='html', description=description)
