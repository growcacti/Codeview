

import tkinter as tk
from tkinter import *
from tkinter import filedialog, Toplevel, Frame, Scrollbar, StringVar
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory

from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import Tk, Button, BOTH, SUNKEN, END
from tkinter.colorchooser import askcolor
import os, sys, subprocess
from tkinter.scrolledtext import ScrolledText 
import re
import runpy
import glob
import time



class Codeview(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)
        self.notebook.add(self.f1, text="View")
        self.fram = tk.Frame(self.f1, width=100, height=20)
        self.fram.grid(row=0, column=0)
        self.f2 = ttk.Frame(self.notebook)
        self.notebook.add(self.f2, text='View2')
        self.lb2 = tk.Listbox(self.f2, bg='cyan2',bd=12, width=35, height=55, exportselection=False, selectmode=tk.SINGLE)
        self.lb2.grid(row=0, column=2)
        self.lb2.focus()
        self.lb2.configure(selectmode="")
        
        self.curtxt = None
        self.x = self.lb2.curselection()
      
        self.flist2 = []
        self.flist = os.listdir(self.path)
    
        for self.item in self.flist:
            if self.item.endswith(".py" or ".txt"):
                self.flist2.append(self.item)

                self.lb2.insert(tk.END, self.item)
         
                self.lb2.focus()
              
      
    
        self.tttx = ScrolledText(self.f2,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.tttx.grid(row = 0, column=6)
    
        



   

        
        self.f3 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f3.grid(row=0, column=1)
        
        self.notebook.add(self.f3, text="Editor")



        self.ttt = ScrolledText(self.f3,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.ttt.grid(row = 0, column=6)
        self.sbf3 = SideButtonframe(self.f3, self.ttt)
        
        self.f4 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f4.grid(row=0, column=1)
        self.notebook.add(self.f4, text="Proof read")
        self.txx = ScrolledText(self.f4,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.txx.grid(row = 0, column=5)
        self.sb2 =SideButtonframe(self.f4, self.txx)
        

        self.f5 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f5.grid(row=0, column=1)
        self.notebook.add(self.f5, text="Snippet")
        self.txxx = ScrolledText(self.f5,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.txxx.grid(row = 0, column=5)
        self.sbf5 =SideButtonframe(self.f5, self.txxx)        
        

        self.lb = tk.Listbox(self.f1, bg='cyan2',bd=12, width=35, height=55, exportselection=False, selectmode=tk.SINGLE)
        self.lb.grid(row=0, column=2)
        self.lb.focus()
        self.lb.configure(selectmode="")
        
        self.curtxt = None
        self.x = self.lb.curselection()
        self.tx = ScrolledText(self.f1,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.tx.grid(row = 0, column=5)
      
        self.flist2 = []
        self.flist = os.listdir(self.path)
    
        for self.item in self.flist:
            if self.item.endswith(".py" or ".txt"):
                self.flist2.append(self.item)

                self.lb.insert(tk.END, self.item)
         
                self.lb.focus()
        self.cvw = Cview_Buttons(self.f1,self.tx,self.lb, self.txx)
        self.cvw2 = Cview_Buttons(self.f2,self.tttx,self.lb2, self.txxx)


       
        self.lb2.bind("<Double-Button-1>", self.cvw2.listing)
        self.lb2.bind("<<ListboxSelect>>", self.cvw2.showcontent)
        self.lb2.bind("<Double-Button-2>", lambda event: self.cvw2.run(self.lb2))
        self.lb2.bind('<<ListboxSelect>>', lambda event: self.cvw2.listing(event))

  
      
       
        self.lb.bind("<Double-Button-1>", self.cvw.listing)
        self.lb.bind("<<ListboxSelect>>", self.cvw.showcontent)
        self.lb.bind("<Double-Button-2>", lambda event: self.cvw.run(self.lb))
        self.lb.bind('<<ListboxSelect>>', lambda event: self.cvw.listing(event))
      

   


    

class FindReplaceWidget:
    
    def __init__ (self, textwidget):
        self.top = Toplevel()
        self.textwidget = textwidget
        self.fr_buttons = ttk.Frame(self.top, relief=tk.RAISED)
       
        
        self.label1 = tk.Label(self.fr_buttons, text ='Find').grid(row=11, column=0)
        self.entry = tk.Entry(self.fr_buttons, width=15,bd=12,bg="wheat")
        self.entry.grid(row=12, column=0)

        self.find1 = tk.Button(self.fr_buttons, text ='Find', bd=8, command=lambda : self.find(self.textwidget))
        self.find1.grid(row=13,column=0)
        self.label2 = tk.Label(self.fr_buttons, text = "Replace With ").grid(row=14, column=0)
        
        self.entry2 = tk.Entry(self.fr_buttons, width=15,bd=12, bg = "seashell")
        self.entry2.grid(row=15, column=0)
        self.entry2.focus_set()
        self.replace1 = tk.Button(self.fr_buttons, text = 'Find&Replace',bd=8,command=lambda : self.find_replace(self.textwidget))
        self.replace1.grid(row=16, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")


    def find(self, textwidget):
        self.textwidget = textwidget
        self.var1 = self.entry.get()
        
    # remove tag 'found' from index 1 to END
        self.textwidget.tag_remove('found', '1.0', END)
       
       #self.finder = self.entry.get()
     
        if (self.var1):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = self.textwidget.search(self.var1, idx, nocase = 1,
                                stopindex = END)
                 
                if not idx: break
                 
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(self.var1))
                 
     
                # overwrite 'Found' at idx
                self.textwidget.tag_add('found', idx, lastidx)
                idx = lastidx
 
        # mark located string as red
         

                self.textwidget.tag_config('found', background ='yellow')
            self.entry.focus.set()        


    

    def find_replace(self,textwidget):
        self.textwidget = textwidget
        self.var1 = self.entry.get()
    
        self.var2 = self.entry2.get()
        
        # remove tag 'found' from index 1 to END
        self.textwidget.tag_remove('found', '1.0', END)
         
        # returns to widget currently in focus
        self.fin = self.var1
        self.repl = self.var2
         
        if (self.fin and self.repl):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = self.textwidget.search(self.fin, idx, nocase = 1,
                                stopindex = END)
                print(idx)
                if not idx: break
                 
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(self.fin))
     
                self.textwidget.delete(idx, lastidx)
                self.textwidget.insert(idx, self.repl)
     
                lastidx = '% s+% dc' % (idx, len(self.repl))
                 
                # overwrite 'Found' at idx
                self.textwidget.tag_add('found', idx, lastidx)
                idx = lastidx
     
            # mark located string as red
            self.textwidget.tag_config('found', foreground ='green', background = 'yellow')
            
class SideButtonframe(ttk.Frame):
    def __init__(self, container, textwidget):
        super().__init__(container)
        self.textwidget = textwidget
        self.parent = container
        self.top = tk.Toplevel()
        self.fr_buttons = tk.Frame(self.parent, relief=tk.RAISED)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
      
        self.btn_open = tk.Button(self.fr_buttons, text="Open",bd=4, command=lambda: self.open_file(self.textwidget))
        self.btn_open.grid(row=1, column=0, pady=5)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", bd=4,command=lambda: self.save_file(self.textwidget))
        self.btn_save.grid(row=2, column=0, pady=5)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear",bd=4, command=lambda: self.clear(self.textwidget))
        self.btn_clear.grid(row=3, column=0, pady=5)
      
        self.ftcolor2 = tk.Button(self.fr_buttons, text="Change FG Color",bd=4, command=lambda: self.changeFg(self.textwidget))
        self.ftcolor2.grid(row=6, column=0, pady=5)
        self.btcolor2 = tk.Button(self.fr_buttons, text="Change BG Color",bd=4, command=lambda: self.changeBg(self.textwidget))
        self.btcolor2.grid(row=7, column=0, pady=5)
        self.btnall = tk.Button(self.fr_buttons, text="Select All", bd=4, command=lambda: self.textwidget.event_generate("<<SelectAll>>"))
        self.btnall.grid(row=8, column=0, pady=5)
        self.btncut = tk.Button(self.fr_buttons, text="Cut", bd=4, command=lambda: self.textwidget.event_generate("<<Cut>>"))
        self.btncut.grid(row=9, column=0, pady=5)
        self.btncopy = tk.Button(self.fr_buttons, text="Copy", bd=4, command=lambda: self.textwidget.event_generate('<<Copy>>'))
        self.btncopy.grid(row=10, column=0, pady=5)
        self.btnpaste = tk.Button(self.fr_buttons, text="Paste", bd=4, command=lambda: self.textwidget.event_generate("<<Paste>>"))
        self.btnpaste.grid(row=11, column=0, pady=5)
        self.btnundo = tk.Button(self.fr_buttons, text="Undo", bd=4, command=lambda: self.undo())
        self.btnundo.grid(row=12, column=0, pady=5)
        self.btnredo = tk.Button(self.fr_buttons, text="Redo", bd=4, command=lambda: self.redo())
        self.btnredo.grid(row=13, column=0, pady=5)
        self.btnfr = tk.Button(self.fr_buttons, text="Find & or Replace", bd=6, command=lambda: self.finder(self.textwidget))
        self.btnfr.grid(row=14, column=0, pady=5)
        self.btninfo = tk.Button(self.fr_buttons, text="Update Info", bd=6, command=lambda: self.update_info)
        self.btninfo.grid(row=15, column=0, pady=5)
        self.bindings()
        self.update_info()


    def update_info(self, event=None):
        self.label = tk.Label(self.fr_buttons, text="             ").grid(row=18, column=0)
        self.label1 = tk.Label(self.fr_buttons, text="             ").grid(row=19, column=0)
        
        self.info_label = tk.Label(self.fr_buttons, text="Lines: 0 | Words: 0 | Characters: 0")
        self.info_label.grid(row=20, column=0)
        # Get the current text content
        content = self.textwidget.get("1.0", "end-1c")

        # Count the lines, words, and characters
        lines = self.textwidget.index("end-1c").split(".")[0]
        words = len(content.split())
        characters = len(content)

        # Update the label with the information
        self.info_label.config(text=f"Lines: {lines} |  \n Words: {words} |\n Characters: {characters}")


    def finder(self, textwidget):
        self.textwidget = textwidget
        fr = FindReplaceWidget(self.textwidget)
        
   
        
    def changeBg(self,textwidget):
            (triple, hexstr) = askcolor()
            if hexstr:
                textwidget.config(bg=hexstr)


    def changeFg(self,textwidget):
        (triple, hexstr) = askcolor()
        if hexstr:
            textwidget.config(fg=hexstr)


    def clear(self, textwidget):
        self.textwidget = textwidget
        self.textwidget.delete("1.0", tk.END)


    def open_file(self,textwidget):
        '''Open a file for editing.'''
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.self.txt'), ('All Files', '*.*')]
        )
        if not filepath:
            return
        textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            textwidget.insert(tk.END, text)
       
    def save_file(self,textwidget):
        '''Save the current file as a new file.'''
        filepath = asksaveasfilename(
            defaultextension='self.txt',
            filetypes=[('Text Files', '*.self.txt'), ('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = textwidget.get(1.0, tk.END)
            output_file.write(text)




    


    def undo(self):
        try:
            
            self.textwidget.edit_undo()
        except:
            print("No previous action")
    def redo(self):
        try:
            self.textwidget.edit_redo()
        except:
            print("No previous action")




    def copy(self, event=None):
        self.clipboard_clear()
        text = self.textwidget.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)


    def select_all(self, event=None):
        self.textwidget.tag_add("sel", "1.0", tk.END)
        return "break"

    def indent2(self,event=None):
        # Get the current line and its content
        index = self.textwidget.index("insert linestart")
        line = self.textwidget.get(index, index + "lineend")

        # Check if the line starts with specific keywords
        keywords = ["if", "elif", "else", "while", "for", "def", "class"]
        if any(line.startswith(keyword) for keyword in keywords):
            # Insert four spaces at the start of the new line
            self.textwidget.insert("insert", " " * 4)
    def auto_indent(self, event=None):
        self.textwidget = event.widget

        # get leading whitespace from current line
        line = self.textwidget.get("insert linestart", "insert")
        match = re.match(r'^(\s+)', line)
        whitespace = match.group(0) if match else ""

        # insert the newline and the whitespace
        self.textwidget.insert("insert", f"\n{whitespace}")

        # return "break" to inhibit default insertion of newline
        return "break"


    def bindings(self):
        self.textwidget.bind("<Return>", self.auto_indent)
        self.textwidget.bind("<Key>", self.update_info)
        self.textwidget.bind("<<Selection>>", self.update_info)


    def quit(self):
        sys.exit(0)


class Cview_Buttons(SideButtonframe):
    def __init__(self, container,textwidget, lb, tx2):
        super().__init__(container, textwidget)
        self.text = textwidget
        self.lb = lb
        self.tx2 = tx2
        self.parent = container
  

        self.dir = tk.Button(self.fr_buttons, text="get dir", bd=4, bg="light pink", command=lambda: self.newdirlist())
        self.dir.grid(row=23, column=0)

        self.btn_grab = tk.Button(self.fr_buttons, text="Send to ",bd=4, bg = "orange", command=lambda: self.ggtxt(self.textwidget))
        self.btn_grab.grid(row=24, column=0)

   
        self.btn_run = tk.Button(self.fr_buttons, text="run py ",bd=4, bg= "light green", command=self.run)
        self.btn_run.grid(row=25, column=0)
       
      

    

    def listing(self,event=None):
        x = event.widget
        try:
            x = int(self.lb.curselection()[0])
            file = self.lb.get(x)
        except IndexError:
         
            v=(self.lb.get(x))
            v =  self.lb.curselection()[0]
            file = self.lb.get(v)
           
        with open(file, "r") as file:
            content = file.read()
            self.textwidget.delete("1.0", tk.END)
            self.textwidget.insert(tk.END, content)
            self.curtxt = content
            return self.curtxt

    def newdirlist(self):
      

        self.path = askdirectory()
        os.chdir(self.path)
        self.flist = os.listdir(self.path)
        self.lb.delete(0, tk.END)

        for self.item in self.flist:

            self.lb.insert(tk.END, self.item)
        return self.flist


    def showcontent(self,x, event=None):
        for i in self.lb.curselection():
            file = self.lb.get(i)
            with open(file, "r") as file:
                file = file.read()
                self.textwidget.delete("1.0", tk.END)
                self.textwidget.insert(tk.END, file)

            return


    def ggtxt(self, tx):
        self.textwidget = tx
        gettxt = self.textwidget.get("1.0", tk.END)
        self.tx2.insert(tk.END, gettxt)


   
    def run(self,listbox):

        self.file = self.listbox.get(ANCHOR)
        runpy.run_module(self.file)
        return




class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        c = Codeview(self)
        self.geometry('1200x1000')
        self.resizable(True, True)

if __name__ == "__main__":
    app=App()
    app.mainloop()

