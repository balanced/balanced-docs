#!/usr/bin/env python
"""
Backends:

    - error
    - enum
    - endpoint
    - view
    - form
    - query

for the `dcode` rST directive.

For example:

    .. dcode: error
        ...

Maps to:

    def error_rst(args):
        ...

"""
import argparse
import logging
import sys

from balanced_docs import BlockWriter, dockers, rst, LogLevelAction


logger = logging.getLogger(__name__)


def form_rst(args):
    content = args.content.read() if args.content else None
    name = args.form[0]
    data = dockers.load(open(args.data, 'r'))
    rst.form.generate(
        writer=BlockWriter(sys.stdout),
        name=name,
        content=content,
        data=data,
        includes=args.includes,
        excludes=args.excludes,
        required=args.required,
    )


def view_rst(args):
    content = args.content.read() if args.content else None
    name = args.view[0]
    data = dockers.load(open(args.data, 'r'))
    rst.view.generate(
        writer=BlockWriter(sys.stdout),
        name=name,
        content=content,
        data=data,
        includes=args.includes,
        excludes=args.excludes,
    )


def endpoint_rst(args):
    content = args.content.read() if args.content else None
    if content:
        logger.warning('discarding content:\n%s', content)
    name = args.endpoint[0]
    data = dockers.load(open(args.data, 'r'))
    rst.endpoint.generate(
        writer=BlockWriter(sys.stdout),
        name=name,
        data=data,
        exclude_methods=args.exclude_methods,
    )


def error_rst(args):
    content = args.content.read() if args.content else None
    if content:
        logger.warning('discarding content:\n%s', content)
    data = dockers.load(open(args.data, 'r'))
    rst.error.generate(BlockWriter(sys.stdout), args.section_char, data, args.sorts)


def enum_rst(args):
    content = args.content.read() if args.content else None
    if content:
        logger.warning('discarding content:\n%s', content)
    name = args.enum[0]
    data = dockers.load(open(args.data, 'r'))
    rst.enum.generate(
        BlockWriter(sys.stdout),
        name,
        data,
        includes=args.includes,
        excludes=args.excludes,
    )

def query_rst(args):
    content = args.content.read() if args.content else None
    name = args.query[0]
    data = dockers.load(open(args.data, 'r'))
    rst.query.generate(
        writer=BlockWriter(sys.stdout),
        name=name,
        content=content,
        data=data,
        includes=args.includes,
        excludes=args.excludes,
    )


# main

class ContentAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        value = values[0]
        content = sys.stdin if value == '-' else open(value)
        setattr(namespace, self.dest, content)


def create_arg_parser():
    # common
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        '-l', '--log-level',
        choices=['debug', 'info', 'warn', 'error'],
        default=logging.INFO,
        action=LogLevelAction,
    )
    common.add_argument(
        '-d', '--data',
        metavar='PATH',
        default='balanced.json',
        help='PATH to data file.',
    )
    common.add_argument(
        '-c', '--content',
        metavar='PATH',
        default=sys.stdin,
        help='PATH to content or - for stdin. Defaults to stdin',
        action=ContentAction,
    )

    parents = [common]
    parser = argparse.ArgumentParser(parents=parents)
    sub_parsers = parser.add_subparsers(title='sub-commands')

    # view
    command = sub_parsers.add_parser('view', parents=parents)
    command.add_argument('view', default=[], nargs=1, metavar='VIEW')
    command.add_argument(
        '-i', '--include',
        dest='includes',
        default=[],
        action='append',
    )
    command.add_argument(
        '-e', '--exclude',
        dest='excludes',
        default=[],
        action='append',
    )
    command.set_defaults(command=view_rst)

    # form
    command = sub_parsers.add_parser('form', parents=parents)
    command.add_argument('form', default=[], nargs=1, metavar='FORM')
    command.add_argument(
        '-i', '--include',
        dest='includes',
        default=[],
        action='append',
    )
    command.add_argument(
        '-e', '--exclude',
        dest='excludes',
        default=[],
        action='append',
    )
    command.add_argument(
        '-r', '--required',
        dest='required',
        default=[],
        action='append',
    )
    command.set_defaults(command=form_rst)

    # endpoint
    command = sub_parsers.add_parser('endpoint', parents=parents)
    command.add_argument('endpoint', default=[], nargs=1, metavar='ENDPOINT')
    command.add_argument(
        '-e', '--exclude-method',
        dest='exclude_methods',
        default=[],
        choices=['GET', 'POST', 'PUT', 'OPTIONS', 'DELETE', 'HEAD'],
        action='append',
    )
    command.set_defaults(command=endpoint_rst)

    # error
    command = sub_parsers.add_parser('error', parents=parents)
    command.add_argument(
        '--section-char',
        default='~',
    )
    command.add_argument(
        '--sort',
        dest='sorts',
        choices=['category_code', 'category_type'],
        default=[],
        action='append',
    )
    command.set_defaults(command=error_rst)

    # enum
    command = sub_parsers.add_parser('enum', parents=parents)
    command.add_argument('enum', default=[], nargs=1, metavar='ENUM')
    command.add_argument(
        '-i', '--include',
        dest='includes',
        default=[],
        action='append',
    )
    command.add_argument(
        '-e', '--exclude',
        dest='excludes',
        default=[],
        action='append',
    )
    command.set_defaults(command=enum_rst)

    # query
    command = sub_parsers.add_parser('query', parents=parents)
    command.add_argument('query', default=[], nargs=1, metavar='QUERY')
    command.add_argument(
        '-i', '--include',
        dest='includes',
        default=[],
        action='append',
    )
    command.add_argument(
        '-e', '--exclude',
        dest='excludes',
        default=[],
        action='append',
    )
    command.set_defaults(command=query_rst)

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

    args.command(args)


if __name__ == '__main__':
    main()
