#!/usr/bin/env python
"""
Extracts content container element from sphinx generated html file.
"""
import sys;
from lxml.html import html5parser, tostring;

parser = html5parser.HTMLParser(namespaceHTMLElements=False);
template = parser.parse(sys.stdin.read());
target = template.xpath('/html/body/div[1]')[0];

print tostring(target)
