import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import subprocess
import shutil
from PIL import Image,ImageTk
#--------------------------------------------------------------------
#Functions and call backs
#--------------------------------------------------------------------

def runpy():
    filerun = lb.curselection()
    
    subprocess.run("/usr/bin/python3", "filerun", shell=True, check=True)
     
def opensystem(event):
    x = lb.curselection()[0]
    os.system(lb.get(x))
    with open(file, 'r') as file:
        file = file.read()
        text.delete('1.0', tk.END)
        text.insert(tk.END, file)
        return
def showcontent(x):
    lb.focus()
    x = lb.curselection()[0]
    file = lb.get(x)
    with open(file, 'r') as file:
        file = file.read()
        text.delete('1.0', tk.END)
        text.insert(tk.END, file)         
        return

     
def sysopen(event):
    x = lbox.curselection()[0]
    os.system(lbox.get(x))
    with open(file, 'r') as file:
        file = file.read()
        text2.delete('1.0', tk.END)
        text2.insert(tk.END, file)
        return
def conshow(x):
    lbox.focus()
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file, 'r') as file:
        file = file.read()
        text2.delete('1.0', tk.END)
        text2.insert(tk.END, file)         
        return
    
#


#-----------------------------------------------------------------------------
# GUI Magic Starts Here
#----------------------------------------------------------------------------

r=tk.Tk()
r.geometry('1800x1080')
r.title("GUI TEMPLATE")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=0)
f1 = ttk.Frame(notebook, width=1500, height=2000)
f1.grid(row=0, column=0)
f1.columnconfigure(2, weight=3)
f1.rowconfigure(6, weight=1)
notebook.add(f1, text='TAB1')

def command():
    pass
def fname():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text.insert(tk.END, text)
 
def guigen():
    import gui_gen



def edit2():
    import editor2
btn2=tk.Button(f1, text='GUI Generator', command=guigen)
btn2.grid(column=1, row=1)
btn3=tk.Button(f1, text='Editor2', command=edit2)
btn3.grid(column=1, row=2)
btn4=tk.Button(f1, text='fname', command=fname)
btn4.grid(column=1, row=3)
btn5=tk.Button(f1, text='RUN', command=runpy)
btn5.grid(column=1, row=4)
btn6=tk.Button(f1, text='button', command=command)
btn6.grid(column=1, row=5)
btn7=tk.Button(f1, text='btn', command=command)
btn7.grid(column=1, row=6)
text = tk.Text(f1, height=250, width=100, bg='cyan')
text.insert('1.0', tk.END)
text.grid(row=0, column=4, rowspan=25, columnspan=10)
##text2 = tk.Text(f1, bg='pink')
##text2.insert('1.0', tk.END)
##text2.grid(row=0, column=0)
###text = tk.Text(f1, bg='light green')
###text.insert('1.0', tk.END)
###text.grid(row=1, column=4, rowspan=25, columnspan=10)
lb = tk.Listbox(f1, bg="yellow", exportselection=False, selectmode=tk.MULTIPLE)
lb.grid(row=0, column=2, rowspan=20, sticky="nswe")
lb.focus()
lb.configure(selectmode="")
flist = os.listdir()
for item in flist:
    lb.insert(tk.END, item)

lb.bind("<<ListboxSelect>>", showcontent)
lb.bind("<Double-Button-1>", opensystem)

#---------------------------------------------------------------------
#Next Tab  TAB2 f2
#---------------------------------------------------------------------
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
def clear():
    txt_edit.delete("1.0", tk.END)
def ggtxt():
    a = text.get("1.0", tk.END)
    txt_edit.insert(tk.END, a)

f2 = ttk.Frame(r)
notebook.add(f2, text='TAB2')

txt_edit = tk.Text(f2, height=200, width=200)
fr_buttons = tk.Frame(f2, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=1, column=0)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_save.grid(row=2, column=0)
btn_clear = tk.Button(fr_buttons, text="Clear", command=clear)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_grab = tk.Button(fr_buttons, text="Grab", command=ggtxt)
btn_grab.grid(row=4, column=0)
#btn_s.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


f3 = ttk.Frame(r)
notebook.add(f3, text='TAB3')
canvas_width = 1800
canvas_height = 900 
w = Canvas(f3, 
           width=canvas_width,
           height=canvas_height)
w.grid(row=0, column=0)
img= ImageTk.PhotoImage(Image.open("screen_locations.png"))
w.create_image(10,10,anchor=NW,image=img)


    


btn1f3=tk.Button(f3, text='Button', command=command)
btn1f3.grid(column=1, row=1)






f4 = ttk.Frame(r)
notebook.add(f4, text='TAB4')
lbox = tk.Listbox(f4, bg="orange", exportselection=True, selectmode=tk.MULTIPLE)
lbox.grid(row=0, column=2, rowspan=20, sticky="nswe")
lbox.focus()
lbox.configure(selectmode="")


path ="/home/jh/CODE_SNIPPETS__/CODE_BASE"

flist1 = os.listdir(path)
for item in flist1:
    lbox.insert(tk.END, item)
lbox.bind("<<ListboxSelect>>", conshow)
lbox.bind("<Double-Button-1>", sysopen)
text2 = tk.Text(f4, bg='pink')
text2.insert('1.0', tk.END)
text2.grid(row=0, column=0)







f5 = ttk.Frame(r)
notebook.add(f5, text='TAB5')
def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


canvas_width = 1800
canvas_height = 900 
w = Canvas(f5, 
           width=canvas_width,
           height=canvas_height)
w.grid(row=0, column=0)

checkered(w,10)






###################################################################
 
r.mainloop()


















































    
