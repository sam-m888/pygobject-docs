=======
Signals
=======

GObject signals are a system for registering callbacks for specific events.

To find all signals of a class you can use the
:func:`GObject.signal_list_names` function:


.. code:: pycon

    >>> GObject.signal_list_names(Gio.Application)
    ('activate', 'startup', 'shutdown', 'open', 'command-line', 'handle-local-options')
    >>> 


To connect to a signal, use :meth:`GObject.Object.connect`:

.. code:: pycon

    >>> app = Gio.Application()
    >>> def on_activate(instance):
    ...     print("Activated:", instance)
    ... 
    >>> app.connect("activate", on_activate)
    17L
    >>> app.run()
    ('Activated:', <Gio.Application object at 0x7f1bbb304320 (GApplication at 0x5630f1faf200)>)
    0
    >>> 

It returns number which identifies the connection during its lifetime and which
can be used to modify the connection.

For example it can be used to temporarily ignore signal emissions using
:meth:`GObject.Object.handler_block`:

.. code:: pycon

    >>> app = Gio.Application(application_id="foo.bar")
    >>> def on_change(*args):
    ...     print(args)
    ... 
    >>> c = app.connect("notify::application-id", on_change)
    >>> app.props.application_id = "foo.bar"
    (<Gio.Application object at 0x7f1bbb304550 (GApplication at 0x5630f1faf2b0)>, <GParamString 'application-id'>)
    >>> with app.handler_block(c):
    ...     app.props.application_id = "no.change"
    ... 
    >>> app.props.application_id = "change.again"
    (<Gio.Application object at 0x7f1bbb304550 (GApplication at 0x5630f1faf2b0)>, <GParamString 'application-id'>)
    >>> 
