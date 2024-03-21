# Description: Makefile for converting SVG files to PDF

SVG_FILES = $(wildcard *.svg)

all: $(SVG_FILES:.svg=.pdf)

.PHONY: all
%.pdf: %.svg
	inkscape -D -z --file=$< --export-pdf=$@

clean:
	rm -f *.pdf
