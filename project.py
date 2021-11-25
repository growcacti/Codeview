# project.py

import tkinter as tk

from tkinter import ttk

from tkinter import simpledialog

from tkinter import messagebox

from tkinter import *

root = tk.Tk()



display1 = tk.StringVar()

entry1 = tk.Entry(root,

    relief=tk.FLAT,

    textvariable=display1,

    justify='right',

    bg='orange')

entry1.pack()

entry1["font"] = "Arial Black 12 bold"

    

b1 = tk.Button(root,

            #relief=tk.FLAT,

            compound=tk.LEFT,

            text="new",

            #command=None,

            #image=tk.PhotoImage("img.png")

            )

b1.pack()


