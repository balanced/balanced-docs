#!/usr/bin/env python
"""
Script used to expand custom rST directives.
"""
import argparse
import logging
from StringIO import StringIO
import sys

from balanced_docs import dcode, DirectiveParser, LogLevelAction

logger = logging.getLogger(__name__)

DIRECTIVES = {
    'dcode-default': dcode.DCodeDefaultDirective,
    'dcode': dcode.DCodeDirective,
}


def expand_directives(fo, disabled):
    directive = None
    for line in fo:
        if not directive:
            name = DirectiveParser.probe(line)
            if name and name in DIRECTIVES and name not in disabled:
                logger.debug('found directive "%s"', name)
                directive = DirectiveParser(
                    name,
                    DIRECTIVES[name].has_content,
                    DIRECTIVES[name].expand,
                )
            else:
                yield line
                continue
        directive(line)
        if not directive.done:
            continue
        logger.debug('expanding directive "%s"', directive.name)
        expansion = [l + '\n' for l in directive.render()]
        for line in expand_directives(expansion, disabled):
            yield line
        if directive.trailer:
            line = directive.trailer
            name = DirectiveParser.probe(line)
            if name and name in DIRECTIVES and name not in disabled:
                logger.debug('found directive "%s"', name)
                directive = DirectiveParser(
                    name,
                    DIRECTIVES[name].has_content,
                    DIRECTIVES[name].expand,
                )
                directive(line)
                continue
            else:
                yield line
        directive = None
    if directive:
        directive('')
        logger.debug('expanding directive "%s"', directive.name)
        expansion = [l + '\n' for l in directive.render()]
        for line in expand_directives(expansion, disabled):
            yield line


DEFAULT_RST = """\

.. dcode-default::

.. dcode-default:: scenario
    :script: ./scripts/http-scenario.py -c scenario.cache
    :section-chars: ~^

.. dcode-default:: view
    :script: ./scripts/rst.py view

.. dcode-default:: form
    :script: ./scripts/rst.py form

.. dcode-default:: endpoint
    :script: ./scripts/rst.py endpoint

.. dcode-default:: error
    :script: ./scripts/rst.py error

.. dcode-default:: enum
    :script: ./scripts/rst.py enum

"""


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'source',
        nargs='?',
        metavar='PATH',
        default=None,
        help='PATH to rST file to expand, otherwise read from stdin.',
    )
    parser.add_argument(
        '-l', '--log-level',
        choices=['debug', 'info', 'warn', 'error'],
        default=logging.INFO,
        action=LogLevelAction,
    )
    parser.add_argument(
        '-d', '--disable',
        dest='disabled',
        metavar='DIRECTIVE',
        help='Disable expansion of DIRECTIVE. None are disabled by default.',
        choices=DIRECTIVES.keys(),
        action='append',
        default=[],
    )
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(args.log_level)

    for line in expand_directives(StringIO(DEFAULT_RST), args.disabled):
        pass

    if args.source == '-':
        fo = sys.stdin
    else:
        fo = open(args.source, 'r')
    for line in expand_directives(fo, args.disabled):
        print line,


if __name__ == '__main__':
    main()
