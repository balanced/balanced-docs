# spec variables
SPEC_SRC_DIR	=	spec/src
SPEC_SRCS		=	$(wildcard $(SPEC_SRC_DIR)/*.rst) $(wildcard $(SPEC_SRC_DIR)/resources/*.rst)
SPEC_RST_DIR	=	spec/dst
SPEC_RST_CMD	=	./spec/build.py
SPEC_RST_DSTS	=	$(addprefix $(SPEC_RST_DIR)/, $(patsubst $(SPEC_SRC_DIR)/%, %, $(SPEC_SRCS)))
SPEC_HTML_DIR	=	site/spec
SPEC_HTML_CMD	=	rst2html.py
SPEC_HTML_DSTS	=	$(addprefix $(SPEC_HTML_DIR)/, $(patsubst %rst, %html, $(patsubst $(SPEC_RST_DIR)/%, %, $(SPEC_RST_DSTS))))

# sphinx public variables (you can set these form the command line).
SPHINXOPTS	=
SPHINXBUILD	= sphinx-build
PAPER 		= n
BUILDDIR	= build

# sphinx internal.
PAPEROPT_a4 	= -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS 	= -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) overview

# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) overview

# common variable
SITE_DIR 			= site

.PHONY: clean spec-clean api-clean all test

all: spec api overview

clean: api-clean spec-clean overview-clean

# spec

test:
	@echo $(SPEC_HTML_DSTS)

$(SPEC_RST_DIR)/%.rst: $(SPEC_SRC_DIR)/%.rst
	@mkdir -p $(@D)
	$(SPEC_RST_CMD) $< > $@

spec-rst: $(SPEC_RST_DSTS)

$(SPEC_HTML_DIR)/%.html: $(SPEC_RST_DIR)/%.rst
	@mkdir -p $(@D)
	$(SPEC_HTML_CMD) $< > $@ 

spec-html: $(SPEC_HTML_DSTS)

spec: spec-rst spec-html

spec-clean:
	-rm -rf $(SPEC_RST_DIR)
	-rm -rf $(SPEC_HTML_DIR)
	-rm -f spec/*.cache

# api

api/html/index.html:
	$(SPHINXBUILD) -b singlehtml -c api api api/html
	
$(SITE_DIR)/api-gen.html: api/html/index.html
	mv api/html/index.html ${SITE_DIR}/api-gen.html

api: $(SITE_DIR)/api-gen.html

api-clean: 
	-rm -rf api/html
	-rm -f $(SITE_DIR)/api-gen.html
	-rm -f *.cache

# overview

overview/html/index.html:
	$(SPHINXBUILD) -b singlehtml -c overview overview overview/html
	
$(SITE_DIR)/overview-gen.html: overview/html/index.html
	mv overview/html/overview.html ${SITE_DIR}/overview-gen.html

overview: $(SITE_DIR)/overview-gen.html

overview-clean: 
	-rm -rf overview/html
	-rm  -f $(SITE_DIR)/overview-gen.html
	-rm -f *.cache
