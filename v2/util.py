import tkinter as t

def add_widget(widget, options=None):
    wid = widget

    if (options != None):
        if 'pack' in options:
            pack_opts = options['pack']

            options.pop('pack')
            wid.config(options)
            wid.pack(pack_opts)
        elif 'grid' in options:
            grid_opts = options['grid']

            options.pop('grid')
            wid.config(options)
            wid.grid(grid_opts)
    else:
        wid.pack()
    
    return wid

def button(container, options=None):
    button = t.Button(container)

    return add_widget(button, options)

def entry(container, options=None):
    entry = t.Entry(container)

    return add_widget(entry, options)

def frame(container, options=None):
    frame = t.Frame(container)

    return add_widget(frame, options)

def label(container, options=None):
    label = t.Label(container)

    return add_widget(label, options)

def listbox(container, options=None):
    listbox = t.Listbox(container)

    return add_widget(listbox, options)

def scrollbar(container, options=None):
    scrollbar = t.Scrollbar(container)

    return add_widget(scrollbar, options)

def window(container, _class):
    window = t.Toplevel(container)
    _class(window)

    return window

def close_window(window):
    window.destroy()