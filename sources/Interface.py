import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.font
import tkinter.ttk
import tkinter.scrolledtext
import unittest
import os

# 1. Message Box
def ShowMessage(msgtitle : str, msgmessage : str):
    tkinter.messagebox.showinfo(title=msgtitle, message=msgmessage)

# 2. File Dialog
def ShowFileDialog() -> os.__file__:
    return tkinter.filedialog.askopenfilename(
        title="Open File",
        initialdir=os.getcwd(),
        filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
    )