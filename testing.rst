==================================
Testing and Continuous integration
==================================

The most important tool to get automated tests of GTK+ code running on a
headless server is Xvfb (virtual framebuffer X server). It provides the
``xvfb-run -a`` command which creates a temporary X server without the need
for any real display hardware.

::

    xvfb-run -a python my_script.py


Example Travis-CI Configuration
-------------------------------

The following example runs your tests under ``xvfb`` and creates one job for
Python2.7 and one for Python3.4. Travis-CI uses Ubuntu 14.04 so you are
limited to these Python versions and to GTK+ 3.10 and PyGObject 3.12.

.. code-block:: yaml

    matrix:
      include:
        - os: linux
          sudo: required
          dist: trusty
          language: generic
          env: PYTHON="python2" PACKAGES="python-gi python-gi-cairo"
        - os: linux
          sudo: required
          dist: trusty
          language: generic
          env: PYTHON="python3" PACKAGES="python3-gi python3-gi-cairo"

    install:
     - sudo apt-get update -q
     - sudo apt-get install --no-install-recommends -y xvfb gir1.2-gtk-3.0 $(echo $PACKAGES)
     - virtualenv --python=$PYTHON --system-site-packages _venv
     - source _venv/bin/activate

    script:
     - xvfb-run -a $PYTHON ./setup.py test
