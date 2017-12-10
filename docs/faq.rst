==========================
Frequently Asked Questions
==========================


Can I use PyGObject with virtualenv?
------------------------------------

To use PyGObject in a virtualenv you have to install it globally and use
``--system-site-packages``.

.. code:: console

    virtualenv --system-site-packages --python=python2 venv
    source venv/bin/activate
    python -c "import gi"
    deactivate

You can also symlink "gi" and "cairo" in the virtualenv, but this is not
supported.


What about the PyGObject package on PyPI?
-----------------------------------------

The `PyGObject <https://pypi.python.org/pypi/PyGObject>`__ on PyPI is the
old PyGObject 2 and should not be used in new projects.


Can I install PyGObject through pip somehow?
--------------------------------------------

You can install directly from git:

.. code:: console

    virtualenv --system-site-packages --python=python2 venv
    source venv/bin/activate
    pip install "git+https://git.gnome.org/browse/pygobject@3.22.0"
    python -c "import gi"
    deactivate

Note that this uses autotools internally and not distutils.


How can I use PyGObject with the official CPython builds on Windows?
--------------------------------------------------------------------

https://sourceforge.net/projects/pygobjectwin32 provides binaries which should
be ABI compatible with the official CPython binaries. I'd recommend using
msys2 if at all possible, since there are more people involved and it's easier
to fix/patch things yourself.
