==================================
Testing and Continuous Integration
==================================


Continuous Integration using Travis CI
--------------------------------------

Travis uses a rather old Ubuntu and thus the supported GTK+ is at 3.10 and
PyGObject is at 3.12. If that's enough for you go ahead.

To get automated tests of GTK+ code running on a headless server is Xvfb
(virtual framebuffer X server). It provides the ``xvfb-run -a`` command which
creates a temporary X server without the need for any real display hardware.

::

    xvfb-run -a python my_script.py


Example Configuration
^^^^^^^^^^^^^^^^^^^^^

The following example runs your tests under ``xvfb`` and creates one job for
Python2.7 and one for Python3.4.

.. code-block:: yaml

    matrix:
      include:
        - os: linux
          sudo: required
          dist: trusty
          language: python
          python: "2.7_with_system_site_packages"
          env: PACKAGES="xvfb gir1.2-gtk-3.0 python-gi python-gi-cairo"
        - os: linux
          sudo: required
          dist: trusty
          language: python
          python: "3.4_with_system_site_packages"
          env: PACKAGES="xvfb gir1.2-gtk-3.0 python3-gi python3-gi-cairo"

    install:
     - sudo apt-get update -q
     - sudo apt-get install --no-install-recommends -y $(echo $PACKAGES)

    script:
     - xvfb-run -a python ./setup.py test
