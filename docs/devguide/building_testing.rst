==================
Building & Testing
==================

Building
--------

Building for Python 2:

::

    ./autogen.sh --with-python=python2
    make

Building for Python 3:

::

    ./autogen.sh --with-python=python3
    make


Testing
-------

To run the test suite::

    make check

To test only a specific class::

    make check TEST_NAMES=test_everything.TestEverything
