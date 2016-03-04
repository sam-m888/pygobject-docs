all: _build

_build: Makefile *.rst conf.py
	sphinx-build -b html . _build

clean:
	rm -R _build
