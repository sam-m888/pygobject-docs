==================
Building & Testing
==================

Building with Autotools
-----------------------

Building for Python 2:

::

    ./autogen.sh --with-python=python2
    make

Building for Python 3:

::

    ./autogen.sh --with-python=python3
    make


Building with Setuptools
------------------------

Building in the source directory:

::

    python setup.py buildext --inplace


Testing
-------

To run the test suite::

    make check

To test only a specific class::

    make check TEST_NAMES=test_everything.TestEverything
