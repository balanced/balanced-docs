from docutils import nodes
from sphinx.writers.html import HTMLTranslator


class BalancedHTMLTranslator(HTMLTranslator):

    def visit_section(self, node):
        # ids = node.get('ids')
        # node['ids'] = []
        self.section_level += 1

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

    def visit_admonition(self, node, name=''):
        self.body.append(self.starttag(
            node, 'div', CLASS=('admonition ' + name)))
        if name and name != 'seealso':
            node.insert(0, nodes.Text(name))

    def visit_desc_addname(self, node):
        '''
        Similar to Sphinx but using a <span> node instead of <tt>.
        '''
        self.body.append(
            self.starttag(node, 'span', '', CLASS='descclassname'))

    def depart_desc_addname(self, node):
        '''
        Similar to Sphinx but using a <span> node instead of <tt>.
        '''
        self.body.append('</span>')

    def visit_desc_name(self, node):
        '''
        Similar to Sphinx but using a <span> node instead of <tt>.
        '''
        self.body.append(self.starttag(node, 'span', '', CLASS='descname'))

    def depart_desc_name(self, node):
        '''
        Similar to Sphinx but using a <span> node instead of <tt>.
        '''
        self.body.append('</span>')

    def visit_literal(self, node):
        '''
        Similar to Sphinx but using a <span> node instead of <tt>.
        '''
        self.body.append(self.starttag(node, 'span', '',
                                       CLASS='docutils literal'))
        self.protect_literal_text += 1

    def depart_literal(self, node):
        '''
        Similar to Sphinx but using a <span> node instead of <tt>.
        '''
        self.protect_literal_text -= 1
        self.body.append('</span>')

    def visit_Text(self, node):
        text = node.astext()
        encoded = self.encode(text)
        if self.protect_literal_text:
            # moved here from base class's visit_literal to support
            # more formatting in literal nodes
            for token in self.words_and_spaces.findall(encoded):
                if token.strip():
                    # protect literal text from line wrapping
                    self.body.append('<code>%s</code>' % token)
                elif token in ' \n':
                    # allow breaks at whitespace
                    self.body.append(token)
                else:
                    # protect runs of multiple spaces; the last one can wrap
                    self.body.append('&nbsp;' * (len(token)-1) + ' ')
        else:
            if self.in_mailto and self.settings.cloak_email_addresses:
                encoded = self.cloak_email(encoded)
            else:
                encoded = self.bulk_text_processor(encoded)
            self.body.append(encoded)
