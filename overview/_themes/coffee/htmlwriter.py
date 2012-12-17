from docutils import nodes
from sphinx.writers.html import HTMLTranslator


class CoffeeThemeHTMLTranslator(HTMLTranslator):

    def visit_section(self, node):
        ids = node.get('ids')
        node['ids'] = []
        HTMLTranslator.visit_section(self, node)
        node['ids'] = ids

    def visit_title(self, node):
        if not isinstance(node.parent, nodes.section):
            HTMLTranslator.visit_title(self, node)
            return

        h_level = self.section_level + self.initial_header_level - 1
        atts = {}
        if (len(node.parent) >= 2 and
            isinstance(node.parent[1], nodes.subtitle)):
            atts['CLASS'] = 'with-subtitle'
        self.body.append(self.starttag(node, 'h%s' % h_level, '', **atts))
        ids = node.parent.get('ids', [])
        for id_ in ids:
            self.body.append('<span id="%s" class="bookmark"></span>' % id_)
        atts = {}
        if node.hasattr('refid'):
            atts['class'] = 'toc-backref'
            atts['href'] = '#' + node['refid']
        if atts:
            self.body.append(self.starttag({}, 'a', '', **atts))
            close_tag = '</a></h%s>\n' % (h_level)
        else:
            close_tag = '</h%s>\n' % (h_level)
        self.context.append(close_tag)

    def visit_container(self, node):
        self.body.append(self.starttag(node, 'div', CLASS='sphinxcontainer'))
