# -*- coding: utf-8 -*-

import sys
import os

extensions = ['sphinx.ext.todo', 'sphinx.ext.intersphinx']

intersphinx_mapping = {
    'gtk': ('https://lazka.github.io/pgi-docs/#Gtk-3.0/', 'https://lazka.github.io/pgi-docs/Gtk-3.0/objects.inv'),
    'gobject': ('https://lazka.github.io/pgi-docs/GObject-2.0', None),
    'glib': ('https://lazka.github.io/pgi-docs/GLib-2.0', None),
    'python': ('http://docs.python.org/2.7', None),
}

source_suffix = '.rst'
master_doc = 'index'
project = u''
copyright = u'2015'
version = '1'
release = '1'
exclude_patterns = ['_build']

pygments_style = 'tango'
html_theme = 'pyramid'
