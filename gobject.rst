=====================================
GObject.Object - The Base Object Type
=====================================

Using methods of the class struct:

Either

::

    >>> Gtk.ContainerClass.list_child_properties(Gtk.Container)
    []
    >>> Gtk.ContainerClass.list_child_properties(Gtk.Box)
    [<GParamBoolean 'expand'>, <GParamBoolean 'fill'>, <GParamUInt 'padding'>, <GParamEnum 'pack-type'>, <GParamInt 'position'>]
    >>> Gtk.ContainerClass.list_child_properties(Gtk.Bin)
    []
    >>> Gtk.ContainerClass.list_child_properties(Gtk.Paned)
    [<GParamBoolean 'resize'>, <GParamBoolean 'shrink'>]

or

::

    >>> Gtk.Container.list_child_properties()
    []
    >>> Gtk.Box.list_child_properties()
    [<GParamBoolean 'expand'>, <GParamBoolean 'fill'>, <GParamUInt 'padding'>, <GParamEnum 'pack-type'>, <GParamInt 'position'>]
    >>> Gtk.Bin.list_child_properties()
    []
    >>> Gtk.Paned.list_child_properties()
    [<GParamBoolean 'resize'>, <GParamBoolean 'shrink'>]
