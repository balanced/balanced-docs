import urllib
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst.roles import set_classes
from sphinx import addnodes
from sphinx.addnodes import compact_paragraph
from sphinx.domains import StandardDomain


def html_page_context(app, pagename, templatename, context, doctree):
    env = app.builder.env

    # toc looks like this:

    # <compact_paragraph toctree="True">
    # ..<bullet_list>
    # ....<list_item classes="toctree-l1">
    # ......<compact_paragraph classes="toctree-l1">
    # ........<reference anchorname="" internal="True" refuri="about/index.html">
    # ..........About
    # ........</reference>
    # ......</compact_paragraph>
    # ....</list_item>


    def on_reference(node):
        # if the node already has an anchorname, it is a subnode
        # so we **want** to make sure the anchor name is the refuri
        # for the node
        if node['anchorname']:
            node['refuri'] = node['refuri']
        else:
            # if not node has an empty anchorname it means that it's the
            # header - so we don't need to have a link, let's just remove
            # it and substitute it with the child text node
            node.parent.replace(
                node,
                # Obviously, node.children[0] here is brittle, but this does
                # it for now. I should really use node.traverse(nodes.text...)
                # and get that node and replace it, but I'm too lazy right now.
                node.children[0]
            )

    # etc; go through and add text inside the <reference>

    def traverse_and_sub_refuri_with_anchorname(node):
        for sub_node in node.children:
            traverse_and_sub_refuri_with_anchorname(sub_node)
        else:
            on_node = {
                'reference': on_reference,
            }.get(node.tagname, None)

            if not on_node:
                return
            on_node(node)

    def render_toctree(**kwargs):
        collapse = kwargs.pop('collapse', False)
        toc = env.get_toctree_for(pagename, app.builder, collapse, **kwargs)

        bullet_lists = toc.traverse(addnodes.nodes.bullet_list)
        bullet_list = bullet_lists[0]
        # the top level <ul> items are bullet_lists and they should have
        # the classes nav and nav-list
        bullet_list.attributes['classes'] = ['nav', 'nav-list', 'context-navlist']

        traverse_and_sub_refuri_with_anchorname(toc)
        r = app.builder.render_partial(toc)['fragment']
        return r

    context['toctree'] = render_toctree


class span(nodes.rubric):
    pass


class Span(Directive):

    name = 'span'

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self):
        set_classes(self.options)
        span_text = self.arguments[0]
        textnodes, messages = self.state.inline_text(span_text, self.lineno)
        _span_node = span(span_text, '', *textnodes, **self.options)
        self.add_name(_span_node)
        return [_span_node] + messages


class Clear(Directive):

    name = 'clear'

    required_arguments = 0
    optional_arguments = 0
    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged}
    has_content = False

    def run(self):

        classes = self.options.get('class', [])
        classes.insert(0, 'clear')
        self.options['class'] = classes
        set_classes(self.options)

        container = nodes.container(classes=classes)
        return [container]


class IconBoxWidget(Directive):

    # Directive

    name = 'icon-box-widget'

    required_arguments = 0

    optional_arguments = 100

    option_spec = {
        'box-classes': directives.unchanged,
        'icon-classes': directives.unchanged,
    }

    has_content = True

    def run(self):
        self.assert_has_content()

        content = ''.join(self.content).strip()

        icon_classes = self.options.get('icon-classes', '')
        icon_classes = icon_classes.split(' ')

        container_classes = self.options.get('box-classes', '')
        container_classes = container_classes.split(' ')

        icons = span(classes=icon_classes)

        node = nodes.container(classes=container_classes)
        node.children.append(icons)

        parsed, _messages = self.state.inline_text(
            content, self.content_offset
        )
        parsed_ = parsed[0]
        for p in parsed[1:]:
            parsed_.children.append(p)

        cp = compact_paragraph('', '', parsed_)
        node.children.append(cp)

        return [node]


class Gist(Directive):

    name = 'gist'

    required_arguments = 1
    optional_arguments = 1
    option_spec = {
        'filename': directives.unchanged
    }

    final_argument_whitespace = False
    has_content = False

    _SCRIPT_TAG = '<script src="{url}"></script>'

    _GIST_URL = 'https://gist.github.com/{gist_path}.js'

    def run(self):
        gist_path = self.arguments[0].strip()
        options = {}
        if 'filename' in self.options:
            options['file'] = self.options['filename']

        url = self._GIST_URL.format(gist_path=gist_path)
        if options:
            url += '?' + urllib.urlencode(options)

        embed_snippet = self._SCRIPT_TAG.format(url=url)
        return [nodes.raw('', embed_snippet, format='html')]


def patch_admonition():
    """
    We're patching the admonition here because docutil's nodes.py covers
    a bunch of node specializations (like warning, note, seealso, etc) and
    they all inherit from the BaseAdmonition class.

    We are adding two options:

    - ``header_class``
    - ``body_class``

    They essentially represent a translation of a:

    .. note::
       :header_class: title
       :body_class: body

       SOME TEXT BODY

    to:

    <div class="title">Note</div>
    <div class="body">SOME TEXT BODY</div>

    """

    BaseAdmonition.option_spec.update({
        'header_class': directives.unchanged,
        'body_class': directives.unchanged,
    })

    def run(self):
        classes = self.options.get('class', [])
        classes.extend(self.options.get('header_class', '').split(' '))
        self.options['class'] = classes
        set_classes(self.options)

        self.assert_has_content()
        text = '\n'.join(self.content)

        admonition_node = self.node_class(text, **self.options)
        self.add_name(admonition_node)
        if self.node_class is nodes.admonition:
            title_text = self.arguments[0]
            textnodes, messages = self.state.inline_text(title_text,
                                                         self.lineno)
            admonition_node += nodes.title(title_text, '', *textnodes)
            admonition_node += messages
            if not 'classes' in self.options:
                admonition_node['classes'] += [
                    'admonition-' + nodes.make_id(title_text)
                ]

        body = nodes.container(
            classes=self.options.get('body_class', '').split(' ')
        )
        self.state.nested_parse(self.content, self.content_offset, body)
        return [admonition_node, body]

    BaseAdmonition._old_run = BaseAdmonition.run
    BaseAdmonition.run = run


def setup(Sphinx):
    Sphinx.connect('html-page-context', html_page_context)
