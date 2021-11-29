import re
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyautogui as pg
import pyperclip
import subprocess
import sys
import os



"""#r is short for root and tk is short for tkinter
# the window is created below with the size
# grid geometry is my prefer pick as I kind of viusualize
# where everything should go
# This auto fill program includes extra imports for when new feature are added"""

r = tk.Tk()
r.title('JH Apps')
r.geometry('800x800')
r.config(bg='#446644')

def chill():
    pass

def update(val):
    #Clear athe list box
    lbox.delete(0, END)
    # listfill to data loop through the now called data
    for item in val:
        lbox.insert(END, item)

def fillout(e):
    #The small e mean event
    # Start off by clearing the entry
    e1.delete(0, END)
    # Then add list as what is clicked from listbox to entry
    # Put in keyword ACTIVE
    e1.insert(0, lbox.get(ACTIVE))
def check(e):
    #grab entry data and check it against the list box
    entered = e1.get()

    if entered == "":
        val = filllist
    else:
        val = []
        for item in filllist:
            # Use the dot .lower keyword command to compare them as both lower case
            if entered.lower() in item.lower():
                #make a new list that is comparable
                val.append(item)

            # in any case the list get compared and needs to be updated
            # the function below is called 
            update(val)    
def clipboardfill():
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(e1.get())
    r.update()
    r.deiconify()
    return

def preclip01():
    govar = e1.get()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(govar)
    r.update()
    r.deiconify()
    pg.hotkey('ctrl', 'alt', 't')
    pg.hotkey('alt', 'tab')  # change window
    pg.hotkey('alt', 'tab')
    pg.hotkey('alt', 'tab')
    pg.hotkey('shift', 'ctrl', 'v')
    #pg.hotkey('shift', 'ctrl', 'v')

def paste():
    #pg.hotkey('alt', 'tab')  # change window
    pg.hotkey('ctrl', 'v')  # ctrl-v to paste
    
   
    return
def copy():
    pg.hotkey('ctrl', 'c')  # ctrl-c to copy
    return
def manager():
    import cb_man
    
def auto1():
     pg.hotkey('alt', 'tab')  # change window
     pg.hotkey('alt', 'tab')
     pg.hotkey('ctrl', 'v')
     pg.press('enter')

def auto2():
    pg.hotkey('alt', 'tab')
    pg.hotkey('shift', 'ctrl', 'v')
def auto3():
    pg.hotkey('alt', 'tab')
    pg.hotkey('ctrl', 'alt', 't')
    pg.hotkey('shift', 'ctrl', 'v')

label=tk.Label(r, text="enter something").grid(row=0, column=2)
#Set up a frame to hoold the widgets
#frame = Frame(r, height=60, width=300)
#frame.grid(row=0, column=0)
#Setup a list box to hold the autocomplete data and show it
lbox = Listbox(r)
lbox.grid(row=5, column=2)
#lbox2 = Listbox(r)
#lbox2.grid(row=5, column=3)


#set and entry widget to to input the data and have it autocomplete possibly
e1 = tk.Entry(r, bg="wheat")
e1.grid(row=1, column=2)
# need a button to trigger an event, and possibly binding later on for
#to trigger different cal;l back functions
btn1 = tk.Button(r, text="send to clipboard", command=clipboardfill)
btn1.grid(row=3, column=1)
btn2 = tk.Button(r, text="auto1", command=auto1)
btn2.grid(row=4, column=1)
btn3 = tk.Button(r, text="auto2", command=auto2)
btn3.grid(row=5, column=1)
btn4 = tk.Button(r, text="auto3", command=auto3)
btn4.grid(row=6, column=1)
btn5 = tk.Button(r, text="autopaste terminal", command=preclip01)
btn5.grid(row=7, column=1)
btn6 = tk.Button(r, text="future event", command=chill)
btn6.grid(row=8, column=1)
btn7 = tk.Button(r, text="add feature", command=chill)
btn7.grid(row=9, column=1)
btn8 = tk.Button(r, text="add feature", command=chill)
btn8.grid(row=10, column=1)
btn9 = tk.Button(r, text="add feature", command=chill)
btn9.grid(row=11, column=1)


# the actual list that is goin to be used for this program if list get big mya
#  consider puitting data in a module and importing it
filllist = ["John", "john.hewitt@cox.net", "john.hewitt@gmail.com", "1073 N 84th Place", "Scottsdale", "Arizona" , "85257", "602-376-2991"]
lbox.bind("<<ListboxSelect>>", fillout)
# "<<ListboxSelect>>" is a keyword that python knows about this binding
e1.bind("<KeyRelease>", check)
update(filllist)
