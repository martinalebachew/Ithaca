SRC_DIR = .
INTERFACE_FILENAME = interface.proto
PYTHON_DST_DIR = ../Parser/python-bridge

.PHONY: all python clean

all: python

python:
	@echo "Compiling Parser Interface for Python..."
	mkdir -p ../Parser/python-bridge
	protoc -I=$(SRC_DIR) --python_out=$(PYTHON_DST_DIR) $(SRC_DIR)/$(INTERFACE_FILENAME)

clean:
	rm -rf $(PYTHON_DST_DIR)
