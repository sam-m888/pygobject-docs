DIAS = $(wildcard images/*.dia)
DIA_SVGS = $(patsubst %.dia,%.svg,$(DIAS))

all: _build

images/%.svg: images/%.dia
	dia $< --export=$@ --filter=dia-svg

_build: Makefile *.rst guide/*.rst conf.py images/*.png $(DIA_SVGS)
	sphinx-build -b html . _build

clean:
	rm -R _build $(DIA_SVGS)
