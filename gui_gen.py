import tkinter as tk
from tkinter import *
import os
import subprocess
import sys

# WIDGETS STRINGS

 

 

entry_counter = 1

button_counter = 1

lbcount = 1

labelcount = 1

cbcount = 1

def entry_code():

    global entry_counter

    w_string = """

display1 = tk.StringVar()

entry1 = tk.Entry(root,

    relief=tk.FLAT,

    textvariable=display1,

    justify='right',

    bg='orange')

entry1.pack()

entry1["font"] = "Arial Black 12 bold"

    """

    w_string2 = w_string.replace("display1", "display" + str(entry_counter))

    w_string2 = w_string2.replace("entry1", "entry" +  str(entry_counter))

    text.insert(tk.END, w_string2)

    entry_counter += 1

 

def button_code():

    global button_counter

    w_string = """

b1 = tk.Button(root,

            #relief=tk.FLAT,

            compound=tk.LEFT,

            text="new",

            #command=None,

            #image=tk.PhotoImage("img.png")

            )

b1.pack()

"""

    w_string2 = w_string.replace("b1", "b" + str(button_counter))

    text.insert(tk.END, w_string2)

    button_counter += 1

 

def label_code():

    global labelcount

    w_str = """ label1 = tk.Label(root)

        

                                  

        label1["font"] = "Arial Black 12 bold"

        label1["fg"] = "#333333",

        label1["justify"] = "center",

        label1["text"] = "label",

        width=100,height=25)

        label1.pack()"""

    w_str2 = w_str.replace("label1", "label" + str(labelcount))

    text.insert(tk.END, w_str2)

    labelcount += 1

   

def listbox_code():

     global lbcount

     w_str = """ lbox1=tk.Listbox(root, width=80, height=25)

        lbox1["borderwidth"] = "1px"

        ft = tkFont.Font(family='Times',size=10)

    

        lbox1["fg"] = "#333333"

        lbox1["justify"] = "center"

        lbox1.pack()"""

def combobox_code():

    global cbcount

    w_str = """ lbox1=tk.Listbox(root, width=80, height=25)

        lbox1["borderwidth"] = "1px"

      

 

        lbox1["fg"] = "#333333"

        lbox1["justify"] = "center"

        lbox1.pack()  """   

 

def save_code():
    
    with open("project.py", "w") as file:
        

        file.write(text.get("0.0", tk.END))
        text.insert(tk.END, "root.mainloop()")
        a = text.get("1.0", tk.END)
        text.insert(tk.END, a)
        with open("project.py", "a") as file:
            a = text.get("1.0", tk.END)
            text.insert(tk.END, a)

    subprocess.run("/usr/bin/idle-python3.7 project.py", shell=True, check=True)
        
        
 

root = tk.Tk()

root.title("Tkinter widget helper")

f1 = tk.Frame(root)

f1.pack(side="left")

b1 = tk.Button(f1, text="entry", command=entry_code)

b1.pack()

 

 

b2 = tk.Button(f1, text="button", command=button_code)

b2.pack()

 

b3 = tk.Button(f1, text="save", command=save_code)

b3.pack()

 

b4 = tk.Button(f1, text="insert label", command=label_code)

b4.pack()

b5 = tk.Button(f1, text="list box", command=listbox_code)

b5.pack()

 

f2 = tk.Frame(root)

f2.pack(side="left")

text = tk.Text(f2)

text.pack()

start_string = """# project.py

import tkinter as tk

from tkinter import ttk

from tkinter import simpledialog

from tkinter import messagebox

from tkinter import *

root = tk.Tk()

"""

text.insert("0.0", start_string)

 

root.mainloop()
