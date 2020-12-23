from tkinter import ttk
from tkinter.constants import *

import tkinter as tk
import util as u

import os

dir_root = os.path.dirname(os.path.realpath('__file__'))
dir_lists = os.path.join(dir_root, 'lists')

listbox_tasks = None

var_width = 30

if not os.path.exists(dir_lists):
    os.makedirs(dir_lists)

class Main:
    def __init__(self, container) -> None:
        self.root = container
        self.root.title('Tasklists')
        self.root.resizable(0, 0)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.menu_file = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_command(label='New Tasklist', command=lambda: self.clear_tasklist(self.treeview_tasks))
        self.menu_file.add_command(label='Load Tasklist', command=lambda: u.window(self.root, Load))
        self.menu_file.add_command(label='Save Tasklist', command=lambda: u.window(self.root, Save))

        self.frame_tasks = u.frame(self.root)
        self.treeview_tasks = u.treeview(self.frame_tasks, {'columns': ('state', 'task'), 'show': 'headings', 'pack': {'side': LEFT}})
        self.scrollbar_tasks = u.scrollbar(self.frame_tasks, {'command': self.treeview_tasks.yview, 'pack': {'side': RIGHT, 'fill': Y}})
        self.treeview_tasks.bind('<Button-1>', self.disable_resize)
        self.treeview_tasks.bind('<Motion>', self.disable_resize)
        self.treeview_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.treeview_tasks.column('state', minwidth=var_width, width=var_width)
        self.treeview_tasks.heading('state', text=u'\u2610')
        self.treeview_tasks.heading('task', text='Task')

        self.frame_add = u.frame(self.root)
        self.button_add_task = u.button(self.frame_add, {'text': 'Add Task', 'command': self.add_task, 'width': 12, 'grid': {'row': 0, 'column': 1}})
        self.entry_add_task = u.entry(self.frame_add, {'grid': {'row': 0, 'column': 0, 'sticky': EW}})
        self.frame_add.grid_columnconfigure(0, weight=1)
        self.frame_add.grid_columnconfigure(1, weight=1)
        self.frame_add.grid_rowconfigure(0, weight=1)
        self.frame_add.grid_rowconfigure(1, weight=1)
        
    def add_task(self):
        print('Testing...')

    def clear_tasklist(self, tasklist):
        tasklist.delete(0, END)
    
    def disable_resize(self, event):
        if self.treeview_tasks.identify_region(event.x, event.y) == 'separator':
            return 'break'

class Load:
    def __init__(self, container) -> None:
        super().__init__()

class Save:
    def __init__(self, container) -> None:
        super().__init__()

root = tk.Tk()
app = Main(root)
root.mainloop()