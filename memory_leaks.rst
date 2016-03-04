======================
Debugging Memory Leaks
======================

GObject Instance Count Leak Check
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requires a development (only available in debug mode) version of glib. Jhbuild
recommended.

::

    jhbuild shell
    GOBJECT_DEBUG=instance-count GTK_DEBUG=interactive ./quodlibet.py

* In the GTK+ Inspector switch to the "Statistics" tab
* Sort by "Cumulative" and do the action which you suspect does leak or where
  you want to make sure it doesn't repeatedly. Like for example opening
  and closing a window or switching between media files to present.
* If something in the "Cumulative" column steadily increases there probably
  is a leak.
