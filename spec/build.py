#!/usr/bin/env python
"""
Script used to generate resource schemas.
"""
import argparse
import json
import logging
import sys

from balanced_docs import LogLevelAction, dockers

logger = logging.getLogger(__name__)


def specs(io, spec_dbs):
    for i, line in enumerate(io):
        # crack
        line = line.strip()
        if not line:
            continue
        parts = line.split(' ')
        if len(parts) != 3:
            raise ValueError(
                '{0}:#{1} is malformed'.format(io.name, i)
            )
        version, type, name = parts
        if version not in spec_dbs:
            raise ValueError(
                '{0}:#{1} has invalid version "{2}"'
                .format(io.name, i, version)
            )
        spec_db = spec_dbs[version]
        match_name = {
            'view': spec_db.match_view,
            'form': spec_db.match_form,
        }
        if type not in match_name:
            raise ValueError(
                '{0}:#{1} has invalid type "{2}"'
                .format(io.name, i, type)
            )
        match = match_name[type](name)
        if not match:
            raise ValueError(
                    '{0}:#{1} no match for "{2}"'
                    .format(io.name, i, line)
                )
        yield match


def json_schema(spec):
    schema = {
        'name': spec['name'],
        'properties': {
        }
    }
    spec_types = {
        'key-value': 'object'
    }
    for field in spec['fields']:
        property = {
            'description': field['description'],
            'required': True,
        }
        property['type'] = spec_types.get(field['type'], field['type'])
        schema['properties'][field['name']] = property
    return schema


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'source',
        nargs='?',
        metavar='FILE',
        default=None,
        help='Spec FILE, otherwise read from stdin.',
    )
    parser.add_argument(
        '-l', '--log-level',
        choices=['debug', 'info', 'warn', 'error'],
        default=logging.INFO,
        action=LogLevelAction,
    )
    parser.add_argument(
        '-s', '--spec',
        default='balanced.json',
        metavar='FILE',
        help='Spec data FILE.',
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

    with open(args.spec, 'r') as fo:
        dbs = json.loads(fo.read())
        spec_dbs = {
            '1.0': dockers.Spec(dbs['rev0']),
            '1.1': dockers.Spec(dbs['rev1']),
        } 
    if args.source == '-':
        fo = sys.stdin
    else:
        fo = open(args.source, 'r')
    for spec in specs(fo, spec_dbs):
        print json.dumps(json_schema(spec), indent=4)


if __name__ == '__main__':
    main()
