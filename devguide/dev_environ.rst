.. include:: ../icons.rst

==================================
Creating a Development Environment
==================================

This describes how to work on PyGObject itself. Please follow the instructions
on ":ref:`gettingstarted`" first, as they are a pre-requirement.

|ubuntu-logo| Ubuntu / |debian-logo| Debian
-------------------------------------------

.. code:: console

    sudo apt build-dep pygobject
    git clone https://git.gnome.org/browse/pygobject
    cd pygobject
    ./autogen.sh
    make
    make check
