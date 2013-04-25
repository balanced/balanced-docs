SRCS=$(wildcard src/*.rst) $(wildcard src/resources/*.rst)
BUILD_DIR=dst
BUILD_CMD=./build.py
DSTS=$(addprefix $(BUILD_DIR)/,$(SRCS))

.PHONY: clean

$(BUILD_DIR)/%.rst: %.rst
	@mkdir -p $(@D)
	$(BUILD_CMD) $< > $@
	
all: $(DSTS) 

clean:
	rm -rf $(BUILD_DIR)
