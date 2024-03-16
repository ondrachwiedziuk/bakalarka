export TEXINPUTS=../tex//:

MARKDOWN_FILES := $(wildcard *.md)

all: $(MARKDOWN_FILES:.md=.tex) prace.pdf clean

%.tex: %.md
	pandoc -L statement.lua --natbib --citeproc $< -o $@

# LaTeX je potreba spustit nekolikrat, aby spravne spocital odkazy
.PHONY: prace.pdf
prace.pdf: prace.tex $(wildcard *.tex) literatura.bib prace.xmpdata
	pdflatex $<
	bibtex prace
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg *.xmpi
	rm -f $(MARKDOWN_FILES:.md=.tex)
