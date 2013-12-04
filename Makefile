REV?= 1.0

# spec variables
SPEC_SRC_DIR	=	spec/src
SPEC_SRCS		=	$(shell find $(SPEC_SRC_DIR)/ -type f -name '*.spec')
SPEC_JS_DIR		=	spec/dst
SPEC_JS_CMD		=	./spec/build.py
SPEC_JS_DSTS 	= $(patsubst $(SPEC_SRC_DIR)/%.spec, $(SPEC_JS_DIR)/%.js, $(SPEC_SRCS))

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
SITE_DIR = site

.PHONY: clean spec-clean api-clean all test all

#all:
#	REV=rev0 make all
#	make clean-limited
#	REV=rev1 make all

all: spec api overview

clean: clean-limited spec-clean
	-rm -rf $(SITE_DIR)/rev*
	-rm -f $(SITE_DIR)/api-gen-*.html
	-rm  -f $(SITE_DIR)/overview-gen-*.html

clean-limited: api-clean overview-clean

rev0:
	REV=rev0 make all

rev1:
	REV=rev1 make all

# spec

$(SPEC_JS_DIR)/%.js: $(SPEC_SRC_DIR)/%.spec
	@mkdir -p $(@D)
	$(SPEC_JS_CMD) $< > $@

spec-js: $(SPEC_JS_DSTS)

spec: spec-js

spec-clean:
	-rm -rf $(SPEC_JS_DIR)

# api

api/html/index.html: $(SITE_DIR)/static/css/styles.css $(SITE_DIR)/static/js/compiled.js
	BALANCED_REV=$(REV) $(SPHINXBUILD) -b dirhtml -c api/$(REV) api/$(REV) api/$(REV)/html

$(SITE_DIR)/api-gen-$(REV).html: api/html/index.html
	mkdir -p ${SITE_DIR}/$(REV)/api
	mv api/$(REV)/html/api ${SITE_DIR}/$(REV)
	#mv api/$(REV)/html/api.html ${SITE_DIR}/api-gen-$(REV).html

api: $(SITE_DIR)/api-gen-$(REV).html

api-clean:
	-rm -rf api/html
	-rm -rf api/rev*/html
	-rm -f *.cache

# overview

overview/html/index.html: $(SITE_DIR)/static/css/styles.css $(SITE_DIR)/static/js/compiled.js
	BALANCED_REV=$(REV) $(SPHINXBUILD) -b dirhtml -c overview/$(REV) overview/$(REV) overview/$(REV)/html

$(SITE_DIR)/overview-gen-$(REV).html: overview/html/index.html
	mkdir -p ${SITE_DIR}/$(REV)
	mv overview/$(REV)/html/overview ${SITE_DIR}/$(REV)
	#mv overview/$(REV)/html/overview.html ${SITE_DIR}/overview-gen-$(REV).html

overview: $(SITE_DIR)/overview-gen-$(REV).html

overview-clean:
	-rm -rf overview/html
	-rm -rf overview/rev*/html
	-rm -f *.cache

# static files

# --line-numbers=mediaquery <-- use this to debug the compiled less
$(SITE_DIR)/static/css/styles.css: $(wildcard $(SITE_DIR)/static/less/*.less)
	./node_modules/.bin/lessc $(SITE_DIR)/static/less/bootstrap.less $@

$(SITE_DIR)/static/js/compiled.js: $(wildcard $(SITE_DIR)/static/js/*.js)
	cat 	$(SITE_DIR)/static/js/bootstrap.min.js 		\
		$(SITE_DIR)/static/js/lunr.min.js 		\
		$(SITE_DIR)/static/js/jquery.scrollTo-min.js 	\
		$(SITE_DIR)/static/js/search.js 		\
		$(SITE_DIR)/static/js/docs.js 			\
			> $@

ddd:
	BALANCED_REV=$(REV) env
	echo $(SPEC_SRCS)