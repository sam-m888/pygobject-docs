all: _build/index.html


_build/index.html: index.rst
	sphinx-build -b html . _build

clean:
	rm -R _build
