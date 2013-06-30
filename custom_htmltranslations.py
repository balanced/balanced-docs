from docutils import nodes
from sphinx.writers.html import HTMLTranslator


class BalancedHTMLTranslator(HTMLTranslator):


    def visit_section(self, node):
        # ids = node.get('ids')
        # node['ids'] = []
        self.section_level += 1

        if self.section_level == 2:
            self.body.append('<hr>\n')
        self.body.append(self.starttag(node, 'section'))

        # node['ids'] = ids

    def depart_section(self, node):
        self.body.append('</section>')
        if self.section_level == 1:
            self.body.append('<hr>\n')

        self.section_level -= 1


    # def visit_title(self, node):
    #
    #     if not isinstance(node.parent, nodes.section):
    #         HTMLTranslator.visit_title(self, node)
    #         return
    #
    #     h_level = self.section_level + self.initial_header_level - 1
    #     atts = {}
    #     if (len(node.parent) >= 2 and
    #         isinstance(node.parent[1], nodes.subtitle)):
    #         atts['CLASS'] = 'with-subtitle'
    #     self.body.append(self.starttag(node, 'h%s' % h_level, '', **atts))
    #     ids = node.parent.get('ids', [])
    #     for id_ in ids:
    #         self.body.append('<span id="%s" class="bookmark"></span>' % id_)
    #     atts = {}
    #     if node.hasattr('refid'):
    #         atts['class'] = 'toc-backref'
    #         atts['href'] = '#' + node['refid']
    #     if atts:
    #         self.body.append(self.starttag({}, 'a', '', **atts))
    #         close_tag = '</a></h%s>\n' % (h_level)
    #     else:
    #         close_tag = '</h%s>\n' % (h_level)
    #     self.context.append(close_tag)

    def visit_span(self, node):
        self.body.append(self.starttag(node, 'span', ''))
    def depart_span(self, node):
        self.body.append('</span>\n')

    def visit_container(self, node):
        self.body.append(self.starttag(node, 'div'))
