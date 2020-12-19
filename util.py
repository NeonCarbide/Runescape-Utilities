import tkinter as tk

def new_button(container, text, command, width=0, side=0):
    if (width > 0):
        button = tk.Button(container, text=text, command=command, width=width)
    else:
        button = tk.Button(container, text=text, command=command)

    if (not isinstance(side, int)):
        button.pack(side=side)
    else:
        button.pack()
    
    return button

def new_entry(container, width=0, side=0):
    if (width > 0):
        entry = tk.Entry(container, width=width)
    else:
        entry = tk.Entry(container)

    if (not isinstance(side, int)):
        entry.pack(side=side)
    else:
        entry.pack()
    
    return entry

def new_grid_entry(container, width=0, row=0, column=0):
    if (width > 0):
        entry = tk.Entry(container, width=width)
    else:
        entry = tk.Entry(container)

    entry.grid(row=row, column=column, padx=5, pady=5)
    
    return entry

def new_frame(container):
    frame = tk.Frame(container)
    frame.pack()

    return frame

def new_grid_button(container, text, command, width=0, row=0, column=0):
    if (width > 0):
        button = tk.Button(container, text=text, command=command, width=width)
    else:
        button = tk.Button(container, text=text, command=command)

    button.grid(row=row, column=column, padx=5, pady=5)
    
    return button

def new_label(container, text, width=0, side=0):
    if (width > 0):
        label = tk.Label(container, text=text, width=width)
    else:
        label = tk.Label(container, text=text)
    
    if (not isinstance(side, int)):
        label.pack(side=side)
    else:
        label.pack()
    
    return label

def new_grid_label(container, text, width=0, row=0, column=0):
    if (width > 0):
        label = tk.Label(container, text=text, width=width)
    else:
        label = tk.Label(container, text=text)
    
    label.grid(row=row, column=column, padx=5, pady=5)
    
    return label

def new_listbox(container, width=0, height=0, side=0):
    if (width > 0):
        if (height > 0):
            listbox = tk.Listbox(container, width=width, height=height)
        else:
            listbox = tk.Listbox(container, width=width)
    else:
        if (height > 0):
            listbox = tk.Listbox(container, height=height)
        else:
            listbox = tk.Listbox(container)
    
    if (not isinstance(side, int)):
        listbox.pack(side=side)
    else:
        listbox.pack()
    
    return listbox

def new_scollbar(container, side=0):
    scrollbar = tk.Scrollbar(container)

    if (not isinstance(side, int)):
        scrollbar.pack(side=side, fill=tk.Y)
    else:
        scrollbar.pack(fill=tk.Y)
    
    return scrollbar

def new_window(container, _class):
    window = tk.Toplevel(container)
    _class(window)

    return window

def clear_listbox(listbox):
    listbox.delete(0, tk.END)

def close_window(window):
    window.destroy()