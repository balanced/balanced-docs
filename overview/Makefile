# You can set these variables from the command line.
SPHINXOPTS	=
SPHINXBUILD	= sphinx-build
PAPER 		= n
BUILDDIR	= build

# Internal variables.
PAPEROPT_a4 	= -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS 	= -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) overview

# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) overview

.PHONY: clean all

overview:
	$(SPHINXBUILD) -b singlehtml -c `pwd` `pwd` `pwd`/html
	@echo
	@echo "Build finished. The HTML pages are in `pwd`/html."

clean:
	-rm -rf `pwd`/html
	-rm -f *.cache

all: overview
