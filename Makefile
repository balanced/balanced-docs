# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS		=
SPHINXBUILD		= sphinx-build
PAPER			=n
BUILDDIR		= build

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

clean: clean-api clean-overview clean-spec

api:
	$(SPHINXBUILD) -b singlehtml -c `pwd`/api api `pwd`/api/html
	@echo
	@echo "Build finished. The HTML pages are in `pwd`/api/html."

clean-api:
	-rm -rf `pwd`/api/html

overview:
	$(SPHINXBUILD) -b singlehtml -c `pwd`/overview overview `pwd`/overview/html
	@echo
	@echo "Build finished. The HTML pages are in `pwd`/overview/html."

clean-overview:
	-rm -rf `pwd`/out/html

spec:
	$(SPHINXBUILD) -b singlehtml -c `pwd`/api api `pwd`/api/html
	@echo
	@echo "Build finished. The HTML pages are in `pwd`/api/html."

clean-spec:
	-rm -rf `pwd`/out/html
