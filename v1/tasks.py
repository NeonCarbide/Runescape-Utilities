from test import listbox
from tkinter.font import Font
from tkinter.messagebox import showwarning as warn
from .util import *

import pickle as p
import tkinter as tk

import os

folder = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'lists')
root_width = 50
listbox_tasks = None

if not os.path.exists(folder):
    os.makedirs(folder)

class Main:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Tasklists')
        self.root.resizable(0, 0)

        self.font_normal = Font(root, family='Segoe UI', size=9, overstrike=False)
        self.font_strikeout = Font(root, family='Segoe UI', size=9, overstrike=True)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.menu_file = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_command(label='New Tasklist', command=lambda: clear_listbox(listbox_tasks))
        self.menu_file.add_command(label='Load Tasklist', command=lambda: new_window(self.root, Load))
        self.menu_file.add_command(label='Save Tasklist', command=lambda: new_window(self.root, Save))

        self.frame_add = new_frame(self.root)
        self.entry_add_task = new_grid_entry(self.frame_add, (root_width - 14), 0, 0)
        self.btn_add_task = new_grid_button(self.frame_add, 'Add Task', self.add_task, 12, 0, 1)

        self.frame_tasks = new_frame(self.root)
        listbox_tasks = new_listbox(self.frame_tasks, root_width, 12, tk.LEFT)
        self.scrollbar_tasks = new_scollbar(self.frame_tasks, tk.RIGHT)
        listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=listbox_tasks.yview)

        self.frame_control = new_frame(self.root)
        self.btn_cross_task = new_grid_button(self.frame_control, 'Cross Task', self.cross_task, 12, 0, 0)
        self.btn_uncross_task = new_grid_button(self.frame_control, 'Uncross Task', self.uncross_task, 12, 0, 2)
        self.btn_remove_task = new_grid_button(self.frame_control, 'Delete Task', self.remove_task, 12, 0, 1)

    def add_task(self):
        task = ' \u2610 : {}'.format(self.entry_add_task.get())

        if (task != ''):
            listbox_tasks.insert(tk.END, task)
            self.entry_add_task.delete(0, tk.END)
        else:
            warn(title='Error', message='No task found\nPlease enter a task')
    
    def remove_task(self):
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except:
            warn(title='Error', message='No task selected\nPlease select a task')

    def cross_task(self):
        try:
            task_index = listbox_tasks.curselection()[0]
            task = ' \u2611 : {}'.format(listbox_tasks.get(task_index).split(': ')[1])
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task)
        except:
            warn(title='Error', message='No task selected\nPlease select a task')

    def uncross_task(self):
        try:
            task_index = listbox_tasks.curselection()[0]
            task = ' \u2610 : {}'.format(listbox_tasks.get(task_index).split(': ')[1])
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task)
        except:
            warn(title='Error', message='No task selected\nPlease select a task')

class Load:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Load Tasklist')
        self.root.resizable(0, 0)

        self.frame_tasklists = new_frame(self.root)
        self.listbox_tasklists = new_listbox(self.frame_tasklists, root_width, 8, tk.LEFT)
        self.scrollbar_tasklists = new_scollbar(self.frame_tasklists, tk.RIGHT)
        self.listbox_tasklists.config(yscrollcommand=self.scrollbar_tasklists.set)
        self.scrollbar_tasklists.config(command=self.listbox_tasklists.yview)

        self.frame_control = new_frame(self.root)
        self.btn_load_tasklist = new_grid_button(self.frame_control, 'Load Tasklist', self.load_tasklist, 12, 0, 0)
        self.btn_cancel = new_grid_button(self.frame_control, 'Cancel', lambda: close_window(self.root), 12, 0, 1)

        self.files = os.listdir(folder)
        self.listbox_tasklists.delete(0, tk.END)

        for file in self.files:
            if (file.split('.')[1] == 'dat'):
                self.listbox_tasklists.insert(tk.END, file.split('.')[0])
    
    def load_tasklist(self):
        try:
            self.tasklist_path = f'{folder}\{self.listbox_tasklists.get(self.listbox_tasklists.curselection()[0])}.dat'
            print(self.tasklist_path)
            self.tasklist = p.load(open(self.tasklist_path, 'rb'))
            print(self.tasklist)
            clear_listbox(listbox_tasks)

            for task in self.tasklist:
                print(task)
                listbox_tasks.insert(tk.END, task)
            
            close_window(self.root)
        except:
            warn()
            # warn(title='Error', message='No tasklist selected\nPlease select a tasklist')

class Save:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Save Tasklist')
        self.root.resizable(0, 0)

        self.frame = new_frame(self.root)
        self.entry = new_grid_entry(self.frame, (root_width - 14), 0, 0)
        self.btn = new_grid_button(self.frame, 'Save', self.save_tasklist, 12, 0, 1)
    
    def save_tasklist(self):
        try:
            self.tasklist_path = f'{folder}\{self.entry.get()}.dat'
            self.tasklist = listbox_tasks.get(0, listbox_tasks.size())
            p.dump(self.tasklist, open(self.tasklist_path, 'wb'))
            self.entry.delete(0, tk.END)
            close_window(self.root)
        except:
            warn(title='Error', message='No tasklist name found\nPlease enter a name for the tasklist')