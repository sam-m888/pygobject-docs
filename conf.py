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
copyright = u'2015'
exclude_patterns = ['_build', 'README.rst']

pygments_style = 'tango'
html_theme = 'sphinx_rtd_theme'
html_show_copyright = False
html_favicon = "images/favicon.ico"
project = "PyGObject"
html_title = project

html_context = {
    'extra_css_files': [
        'https://quodlibet.github.io/fonts/font-mfizz.css',
        '_static/extra.css',
    ],
}

html_static_path = [
    "extra.css",
    "images/pygobject-small.svg",
]

html_theme_options = {
    "display_version": False,
}
