=================
Development Guide
=================

.. toctree::
    :titlesonly:
    :maxdepth: 1

    style_guide


Reporting Bugs
--------------

You can search through the GNOME Bugzilla for existing bug reports:
https://bugzilla.gnome.org/page.cgi?id=browse.html&product=pygobject

You can also file a new bug report:
https://bugzilla.gnome.org/enter_bug.cgi?product=pygobject


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


If you need newer versions of dependencies it's recommended to use JHBuild::

    jhbuild build pygobject pygobject-python2


If you want to test against different Python versions and happend to be on
Ubuntu you can use the following PPA to get older Python versions::

    sudo add-apt-repository ppa:fkrull/deadsnakes


Testing
-------

To run the test suite::

    make check

To skip pep8 tests::

    make check SKIP_PEP8=1

To test only a specific class::

    make check TEST_NAMES=test_everything.TestEverything


Submitting Patches
------------------

Make your changes and commit them. Use the following to export the, for
example, the last 3 commits::

    git format-patch -3

Open a new bug report and attach the resulting files.
