# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS		=
SPHINXBUILD		= sphinx-build
PAPER			=n
BUILDDIR		= build
S3PUBLISH		= s3.py upload justice.web --public

define SPHINXCONTAINER
python -c \
"import sys; \
from lxml.html import html5parser, tostring; \
parser = html5parser.HTMLParser(namespaceHTMLElements=False); \
template = parser.parse(sys.stdin.read()); \
target = template.xpath('/html/body/div[1]')[0]; \
print tostring(target) \
"
endef

SRC_DIR=spec/src
SRC_FILES=$(wildcard $(SRC_DIR)/*.rst) $(wildcard $(SRC_DIR)/resources/*.rst)

BUILD_DIR=${BUILDDIR}

RST_DIR=$(BUILD_DIR)/rst
RST_BUILD=./scripts/builder
RST_FILES=$(foreach file,$(SRC_FILES),$(subst $(SRC_DIR),$(RST_DIR),$(file)))

HTML_DIR=$(BUILD_DIR)/html
HTML_FILES=$(foreach file,$(RST_FILES),$(subst $(RST_DIR),$(HTML_DIR),$(file:.rst=.html)))
RST_2_HTML=./scripts/rst2html.py


# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) overview
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) overview

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext refclean api overview

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"

clean: clean-api clean-overview
	-rm -rf $(BUILDDIR)/*

rmcache:
	-rm -rf cache.json

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

api:
	$(SPHINXBUILD) -b singlehtml -c `pwd`/api api `pwd`/api/html
	@echo
	@echo "Build finished. The HTML pages are in `pwd`/api/html."

clean-api:
	-rm -rf `pwd`/api/html

preview-api: api
	$(SPHINXCONTAINER) < `pwd`/api/html/index.html > /tmp/api.html && echo '/tmp/api.html docs/api-preview.html' | $(S3PUBLISH)
	@echo
	@echo "Previewed api."

publish-api: api
	$(SPHINXCONTAINER) < `pwd`/api/html/index.html > /tmp/api.html && echo '/tmp/api.html docs/api.html' | $(S3PUBLISH)
	@echo
	@echo "Published api."

overview:
	$(SPHINXBUILD) -b singlehtml -c `pwd`/overview overview `pwd`/overview/html
	@echo
	@echo "Build finished. The HTML pages are in `pwd`/overview/html."

clean-overview:
	-rm -rf `pwd`/overview/html

preview-overview:
	$(SPHINXCONTAINER) < `pwd`/overview/html/index.html > /tmp/overview.html && echo '/tmp/overview.html docs/overview-preview.html' | $(S3PUBLISH)
	@echo
	@echo "Preview overview."

publish-overview: overview
	$(SPHINXCONTAINER) < `pwd`/overview/html/index.html > /tmp/overview.html && echo '/tmp/overview.html docs/overview.html' | $(S3PUBLISH)
	@echo
	@echo "Published overview."

rst: $(RST_FILES)

$(RST_DIR)/%.rst: $(SRC_DIR)/%.rst
	@mkdir -p $(@D)
	$(RST_BUILD) $< > $@

html: $(HTML_FILES)

$(HTML_DIR)/%.html: $(RST_DIR)/%.rst
	@mkdir -p $(@D)
	$(RST_2_HTML) $< $@
