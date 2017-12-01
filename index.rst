.. include:: icons.rst

.. title:: Overview

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 1

    getting_started
    guide/index

    faq
    deploy
    testing
    debug_profile
    porting
    devguide/index
    maintguide
    further
    contact

.. image:: images/pygobject.svg
   :align: center
   :width: 400px
   :height: 98px

|

**PyGObject** is a Python package which provides bindings for `GObject
<https://developer.gnome.org/gobject/stable/>`__ based libraries such as `GTK+
<https://www.gtk.org/>`__, `GStreamer <https://gstreamer.freedesktop.org/>`__,
`WebKitGTK+ <https://webkitgtk.org/>`__, `GLib
<https://developer.gnome.org/glib/stable/>`__, `GIO
<https://developer.gnome.org/gio/stable/>`__ and many more.

If you want to write a Python application for `GNOME
<https://www.gnome.org/>`__ or a Python GUI application using GTK+, then
PyGObject is the way to go. Also check out the "`Python GTK+ 3 Tutorial
<https://python-gtk-3-tutorial.readthedocs.io>`__" and the "`Python GI API
Reference <https://lazka.github.io/pgi-docs>`__".


How does it work?
-----------------

.. figure:: images/overview.svg
    :width: 600px
    :height: 222px
    :align: center

PyGObject uses `glib <https://developer.gnome.org/glib/stable/>`__, `gobject
<https://developer.gnome.org/gobject/stable/>`__, `girepository
<https://developer.gnome.org/gi/stable/>`__, `libffi
<https://sourceware.org/libffi/>`__ and other libraries to access the C
library (libgtk-3.so) in combination with the additional metadata from the
accompanying typelib file (Gtk-3.0.typelib) and dynamically provides a Python
interface based on that information.


Who Is Using PyGObject?
-----------------------

* `D-Feet <https://wiki.gnome.org/action/show/Apps/DFeet>`__ - an easy to use D-Bus debugger
* `GNOME Music <https://wiki.gnome.org/Apps/Music>`__ - a music player for GNOME
* `GNOME Tweak Tool <https://wiki.gnome.org/action/show/Apps/GnomeTweakTool>`__ - a tool to customize advanced GNOME 3 options
* `Gramps <https://gramps-project.org/>`__ - a genealogy program
* `Lollypop <https://gnumdk.github.io/lollypop-web/>`__ - a modern music player
* `Meld <http://meldmerge.org/>`__ - a visual diff and merge tool
* `MyPaint <http://mypaint.org/>`__ - a nimble, distraction-free, and easy tool for digital painters
* `Orca <https://wiki.gnome.org/Projects/Orca>`__ - a flexible and extensible screen reader
* `Pithos <https://pithos.github.io/>`__ - a Pandora Radio client
* `Pitivi <http://www.pitivi.org/>`__ - a free and open source video editor
* `Quod Libet <https://quodlibet.readthedocs.io/>`__ - a music library manager / player
* `Transmageddon <http://www.linuxrising.org/>`__ - a video transcoder
* `Pithos <https://pithos.github.io/>`__ - an unoffical Pandora radio client


The following applications or libraries use PyGObject for optional features,
such as plugins or as optional backends:

* `beets <http://beets.io/>`__ - a music library manager and MusicBrainz tagger
* `gedit <https://wiki.gnome.org/Apps/Gedit>`_- a GNOME text editor
* `matplotlib <http://matplotlib.org/>`__ - a python 2D plotting library
* `Totem <https://wiki.gnome.org/Apps/Videos>`__ - a video player for GNOME
