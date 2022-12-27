# Copyright 2022 Manna Harbour
# https://github.com/manna-harbour/miryoku

source := $(wildcard *.py.cpp)

all: $(source:%.py.cpp=build/%.py)

build/%.py: %.py.cpp *.h *.mk makefile miryoku_babel/*
	cpp -P $(OPT_DEFS) $< | \
	sed \
	  -e 's/U_HASH/#/g' \
	  -e 's/[ ]*U_LF[ ]*/\n/g' \
	  -e 's/[ ]*U_TAB[ ]*/\t/g' \
	 > $@

include custom_rules.mk

include post_rules.mk

