
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Version: 3.7.5
#
# Author: Steven J. Carney
#
# Title: The Chalice of Torres
#
# Tested OS: This code is known to work on WIndows 10
#

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import Chalice_Fun
import Chalice_Gui



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.filename = 'Test'
        self._filetypes = [
        ('Text', '*.txt'),
            ('All files', '*'),
            ]

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) # (Height, Width)
        #self.master.maxsize(1000,600)
        self.master.resizable(True, True)
        # This CenterWindow method will center our app on the user's screen
        Chalice_Fun.center_window(self,1000,600)
        self.master.title("The Chalice of Torres")
        self.master.configure(bg="darkgrey")
        # This protocol method is a tkinter built-in method to catch if
        # the user 
        # clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: Chalice_Fun.ask_quit(self))
        arg = self.master
        
        #Sets textbox for output


                # load in the GUI widgets from a separate modules,
        # keeping the code compatmentalized and clutter free
        Chalice_Gui.load_GUI(self)
                
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
#        filemenu.add_command(label="Save", command=save_file(self))
#        filemenu.add_command(label="Save As")#, command=save_file_as(self))
#        filemenu.add_command(label="Open")#, command=open_file(self))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: Chalice_Fun.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About The Chalice of Torres") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        self.master.config(menu=menubar, borderwidth='1')


"""
def save_file(self, whatever = None):
    if (self.filename == ''):
        save_file_as(self)
    else:
        f = open(self.filename, 'w')


def save_file_as(self, whatever = None):
    self.filename = tk.filedialog.asksaveasfilename(defaultextension='.txt',filetypes = self._filetypes)
    f = open(self.filename, 'w')
    f.write(self.get('1.0', 'end'))

def open_file(self, whatever = None, filename = None):
    if not filename:
        self.filename = tk.filedialog.askopenfilename(filetypes = self._filetypes)
    else:
        self.filename = filename
    if not (self.filename == ''):
        f = open(self.filename, 'r')
        f2 = f.read()
        self.delete('1.0', 'end')
        self.insert('1.0', f2)
        self.title('Load_GUI %s)' % self.filename)
"""

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
