REV? = rev1
REV_NUM? = 1.1

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
ASSET_DIR = assets
BUILD_DIR = build

.PHONY: clean cache-clean api-clean clean-limited build-revisions all test all bowerize compile-less compile-js cp-static pkg-old-revisions api overview

build-revisions: clean-build prep-dirs bowerize compile-less compile-js cp-static api overview pkg-old-revisions

all: rev1

cache-clean:
	-rm -f *.cache

clean: cache-clean clean-limited clean-build

clean-limited: api-clean overview-clean

clean-build:
	-rm -rf $(BUILD_DIR)
	-rm -rf $(ASSET_DIR)/bower_components

prep-dirs:
	mkdir $(BUILD_DIR)
	mkdir $(BUILD_DIR)/static
	mkdir $(BUILD_DIR)/static/css
	mkdir $(BUILD_DIR)/static/js

cp-static:
	cp -r $(ASSET_DIR)/img $(BUILD_DIR)/static/img
	cp -r $(ASSET_DIR)/fonts $(BUILD_DIR)/static/fonts

pkg-old-revisions:
	cp -r $(ASSET_DIR)/doc-archives/* $(BUILD_DIR)/

rev1:
	REV=rev1 REV_NUM=1.1 make build-revisions

# api

api:
	BALANCED_REV=$(REV) $(SPHINXBUILD) -b dirhtml -c api/$(REV) api/$(REV) api/$(REV)/html
	mkdir -p $(BUILD_DIR)/$(REV_NUM)/api
	mv api/$(REV)/html/api $(BUILD_DIR)/$(REV_NUM)

api-clean:
	-rm -rf api/html
	-rm -rf api/rev*/html
	-rm -f *.cache

# overview
	
overview:
	BALANCED_REV=$(REV) $(SPHINXBUILD) -b dirhtml -c overview/$(REV) overview/$(REV) overview/$(REV)/html
	mkdir -p $(BUILD_DIR)/$(REV_NUM)/overview
	mv overview/$(REV)/html/overview $(BUILD_DIR)/$(REV_NUM)
	-mv overview/$(REV)/html/guides $(BUILD_DIR)/$(REV_NUM)

overview-clean:
	-rm -rf overview/html
	-rm -rf overview/rev*/html
	-rm -f *.cache

# static files
bowerize:
	bower install --allow-root --config.interactive=false strapped
	cp -r $(ASSET_DIR)/bower_components/strapped/static/less $(ASSET_DIR)/less/strapped
	cp -r $(ASSET_DIR)/bower_components/strapped/static/fonts $(ASSET_DIR)/fonts
	cp -r $(ASSET_DIR)/bower_components/strapped/static/images $(ASSET_DIR)/img

compile-less: $(wildcard $(ASSET_DIR)/less/*.less)
	lessc $(ASSET_DIR)/less/base.less > $(BUILD_DIR)/static/css/styles.css

compile-js:
	cat $(ASSET_DIR)/js/bootstrap.min.js 		\
		$(ASSET_DIR)/js/lunr.min.js 		\
		$(ASSET_DIR)/js/jquery.scrollTo-min.js 	\
		$(ASSET_DIR)/js/jquery-cookie.js 	\
		$(ASSET_DIR)/js/search.js 		\
		$(ASSET_DIR)/js/docs.js 			\
		$(ASSET_DIR)/js/google-analytics.js 			\
			> $(BUILD_DIR)/static/js/compiled.js

ddd:
	BALANCED_REV=$(REV) env
	echo $(SPEC_SRCS)