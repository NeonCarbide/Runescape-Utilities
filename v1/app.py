from .util import *
from . import tasks
from . import timers

import tkinter.ttk as ttk
import tkinter as tk

import psutil

def isRunescapeOpen():
    for proc in psutil.process_iter():
        try:
            if 'runescape' in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return False

root = tk.Tk()
root.title('Runescape Tools')
root.resizable(0, 0)

frame_main = new_frame(root)

btn_game = tk.Button(frame_main, width=30)
btn_game.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

if (not isRunescapeOpen()):
    btn_game['state'] = 'active'
    btn_game['text'] = 'Launch Runescape'
else:
    btn_game['state'] = 'disabled'
    btn_game['text'] = 'Running...'

h_line = ttk.Separator(frame_main, orient='horizontal')
h_line.grid(row=1, column=0, columnspan=2, padx=10, sticky='ew')

label_tasklists = new_grid_label(frame_main, 'Tasklists', 30, 2, 0)
btn_tasklists = new_grid_button(frame_main, 'Launch', lambda: new_window(root, tasks.Main), 12, 2, 1)

label_timers = new_grid_label(frame_main, 'Farming Timers', 30, 3, 0)
btn_timers = new_grid_button(frame_main, 'Launch', lambda: new_window(root, timers.Main), 12, 3, 1)

root.mainloop()
