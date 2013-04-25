#!/usr/bin/env python
import argparse
import logging
from StringIO import StringIO
import sys

from balanced_docs import dcode, DirectiveParser

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
        for line in directive.render():
            yield line
            yield '\n'
        yield '\n'
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
        for line in directive.render():
            yield line
            yield '\n'
        yield '\n'


DEFAULT_RST = """\

.. dcode-default::
    :cache:
    :directive: code-block

.. dcode-default:: scenario
    :script: scenario.py -c scenario.cache -d scenarios
    :ignore:
    :section-chars: ^
    :section-depth: 2

.. dcode-default:: view
    :script: ./rst.py view

.. dcode-default:: form
    :script: ./rst.py form

.. dcode-default:: endpoint
    :script: ./rst.py endpoint

.. dcode-default:: error
    :script: ./rst.py error

.. dcode-default:: enum
    :script: ./rst.py enum

"""


class LogLevelAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        level = getattr(logging, values.upper())
        setattr(namespace, self.dest, level)


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('source',
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
    parser.add_argument('-d', '--disable',
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
