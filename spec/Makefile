SRC_DIR=src
SRCS=$(wildcard $(SRC_DIR)/*.rst) $(wildcard $(SRC_DIR)/resources/*.rst)
BUILD_DIR=dst
BUILD_CMD=./build.py
DSTS=$(addprefix $(BUILD_DIR)/, $(patsubst $(SRC_DIR)/%, %, $(SRCS)))

.PHONY: clean

$(BUILD_DIR)/%.rst: $(SRC_DIR)/%.rst
	@mkdir -p $(@D)
	$(BUILD_CMD) $< > $@
	
all: $(DSTS) 

clean:
	rm -rf $(BUILD_DIR)
	rm *.cache
