all: _build

_build: Makefile *.rst
	sphinx-build -b html . _build

clean:
	rm -R _build
