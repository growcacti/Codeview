'''
Quick Start for tkinter Toys Starter Set
     This code performs 2 functions: (1) it makes an effort to provide
inclusive examples of many essential process, syntax and structures and
(2) it provides a good starting place work area for experimenting with
options, attributes, other widgets, methods and commands.
'''
from tkinter import *   # With "import tkinter as tk" must preface all commands
root=Tk()   # Job1" initialize tkinter with a root screen.
root.wm_attributes("-fullscreen", True)   # New (TCL8.4) easy way to fill screen.
root.configure(background='snow3')   # Add a neutral color mat to the root.
 
# Establish your functions in one area for a clean structure.
def egress():   # Provide a function to close the app - normally not on the root,
    root.destroy()  # but this is a special case for demo and experimenting.
 
def textInput(event):             # We want a prompt in the entry widget
    e1.delete(0,END)              # but when the user if finished we don't want
    e1.unbind("<Key>")            # the input message in the string we retrieve,
    e1.bind("<Return>", useInput) # so we intercept the first key stroke, clear the
    e1.insert(0, e1.get())        # display, unbind keypress, bind <Return>, and re-
                                  # establish out input line begining with the
                                  # keypress captured by our entry widget.
def useInput(self):               # Now when <Return> is pressed this function gets
    L1Text.set(e1.get())          # it in a control variable that updates our label,
    e1.delete(0,END)              # clears the line, sets a new prompt, rebinds <Key>,
    e1.insert(0, "Line "+ str(Counter.get()) + ":  ")
    e1.bind("<Key>", textInput)
    Counter.set(Counter.get()+1)  # and updates a counter tracking our line number.
 
# Housekeeping: in this area we do things like define some control variables
EnterPrompt=StringVar()
akey=StringVar()
L1Text=StringVar()
Counter=IntVar()
 
EnterPrompt.set("Enter something: ")  # the first prompt we will use
akey.set("")
L1Text.set("")
Counter.set(2)  # set counter to 2 - thats the first line where it will be used
 
#     Time now to create our windows and widgets, starting with our toplevel window
top1 = Toplevel(root, bg="light blue")  # toplevel is one of the containers that
top1.geometry('800'+'x'+'400')          # should normally hold all our widgets
top1.title("top1 Window: Starter Set Test Layout")   # we can put a title on it and
top1.attributes("-topmost", 1)  # need to make sure top1 is on top of other windows 
 
# Now we create the exit button  - note the "\" lets us break and continue a line
bexit=Button(root, command=egress, text="Close\rButton",  bg="brown",fg="white",\
              font=("Calibi 14 bold"), width=10, height=2)
# ...and here we use the "pack" geometry manager to place it on the screen
bexit.pack(ipady=2, ipadx=2, pady=3, padx=3,side="left", anchor="nw")
 
# This is the entry widget that lets us input/display a SINGLE LINE.
e1=Entry(top1, width=50, bg="beige", textvariable=EnterPrompt)
e1.bind("<Key>", textInput)  # the <Key> binding lets us capture any keypress
e1.focus_set()
e1.icursor(END)     # the icursor method lets us go to the end of the prompt
e1.pack(pady=80)    # and again we use the pack geometry with an 80 pix y axis pad
 
# The last widget is just a label which shows whatever "L1Text" variable holds
L1Text.set("Starter Set: Basic test layout")
l1=Label(top1, textvariable=L1Text, width = 50)     #50 characters wide, like e1
l1.pack(anchor= "center", side="bottom", pady=80)   #force to bottom with a cushion
 
mainloop()     #last but not least - nothing happens without a mainloop bound
