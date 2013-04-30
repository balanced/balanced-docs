#!/usr/bin/env python
"""
Backend for the scenario dcode rST directive.

For example:

    .. dcode: scenario
        ...

Maps to:

    def main():
        ...

"""
import argparse
import logging
import sys

from balanced_docs import LogLevelAction


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'scenarios',
        nargs='+',
        metavar='SCENARIO',
        help='Name of the SCENARIO to run.',
    )
    parser.add_argument(
        '-l', '--log-level',
        choices=['debug', 'info', 'warn', 'error'],
        default=logging.INFO,
        action=LogLevelAction,
    )
    parser.add_argument(
        '-c', '--cache',
        metavar='PATH',
        default=None,
        help='PATH to scenario context cache file. No caching by default.',
    )
    parser.add_argument(
        '--sections',
        metavar='CHARS',
        default='~^',
        help='String of CHARS to use for section headings.',
    )
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    root = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    root.addHandler(handler)
    root.setLevel(args.log_level)


if __name__ == '__main__':
    main()
