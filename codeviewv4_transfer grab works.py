import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import subprocess
import shutil
#--------------------------------------------------------------------
#Functions and call backs
#--------------------------------------------------------------------


     
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
def map():
    import ScreenMap
btn1=tk.Button(f1, text='map', command=map)
btn1.grid(column=0, row=0)
btn2=tk.Button(f1, text='btn1', command=command)
btn2.grid(column=1, row=0)
btn3=tk.Button(f1, text='button2', command=command)
btn3.grid(column=0, row=2)
btn4=tk.Button(f1, text='button2', command=command)
btn4.grid(column=1, row=2)
btn5=tk.Button(f1, text='button2', command=command)
btn5.grid(column=0, row=4)
btn6=tk.Button(f1, text='button3', command=command)
btn6.grid(column=0, row=5)

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











f4 = ttk.Frame(r)
notebook.add(f4, text='TAB4')
f5 = ttk.Frame(r)
notebook.add(f5, text='TAB5')
f6 = ttk.Frame(r)
notebook.add(f6, text='TAB6')

























































# TAB2 Function build gui parts
##f2 = ttk.Frame(notebook, width=1500, height=2000)
##f2.grid(row=0, column=0)
## # layout on the root window
##f2.columnconfigure(0, weight=4)
##f2.row.configure(1, weight=1)
##notebook.add(f2, text='TAB2')
##def create_input_frame(f2):
##
##    ff1 = ttk.Frame(r)
##
##    # grid layout for the input frame
##    ff1.columnconfigure(0, weight=1)
##    ff1.columnconfigure(0, weight=3)
##
##    # Label in this frame 2nd column 1st row 
##    ttk.Label(ff1, text='txt').grid(column=0, row=0, sticky=tk.W)
##    keyword = ttk.Entry(ff1, width=30)
##    keyword.focus()
##    keyword.grid(column=1, row=0, sticky=tk.W)
##
##    # Label 2nd column 2nd row
##    ttk.Label(ff1, text='txt').grid(column=0, row=1, sticky=tk.W)
##    replacement = ttk.Entry(ff1, width=30)
##    replacement.grid(column=1, row=1, sticky=tk.W)
##
##    # Checkbox 1st column 3rd row
##    match_case = tk.StringVar()
##    match_case_check = ttk.Checkbutton(
##        ff1,
##        text='txt',
##        variable=match_case,
##        command=lambda: print(match_case.get()))
##    match_case_check.grid(column=0, row=2, sticky=tk.W)
##def create_button_frame(ff1):
##    ff2 = ttk.Frame(container)
##
##    ff2.columnconfigure(0, weight=1)
##
##    ttk.Button(ff2, text='add text').grid(column=0, row=0)
##    ttk.Button(ff2, text='add txt').grid(column=0, row=1)
##    ttk.Button(ff2, text='txt').grid(column=0, row=2)
##    ttk.Button(ff2, text='txt').grid(column=0, row=3)
##
##    for widget in ff2.winfo_children():
##        widget.grid(padx=0, pady=3)
##
##    return ff2
##
##
##ff1 = create_input_frame(f2)
##ff1.grid(column=0, row=0)
##
##ff2 = create_button_frame(f2)
##ff2.grid(column=1, row=0)
##def file_manager():
##     # Creating the backend functions for python file explorer project
##    def open_file():
##        file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])
##        os.startfile(os.path.abspath(file))
##    def copy_file():
##        file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
##        dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")
##        try:
##            shutil.copy(file_to_copy, dir_to_copy_to)
##            mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
##        except:
##            mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')
##    def delete_file():
##        file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])
##        os.remove(os.path.abspath(file))
##        mb.showinfo(title='File deleted', message='Your desired file has been deleted')
##    def rename_file():
##        file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])
##        rename_wn = Toplevel(r)
##        rename_wn.title("Rename the file to")
##        rename_wn.geometry("250x70"); rename_wn.resizable(0, 0)
##        Label(rename_wn, text='What should be the new name of the file?', font=("Times New Roman", 10)).grid(row=0, column=0)
##        new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
##        new_name.grid(row=1, column=1)
##        new_file_name = os.path.join(os.path.dirname(file), new_name.get()+os.path.splitext(file)[1])
##        os.rename(file, new_file_name)
##        mb.showinfo(title="File Renamed", message='Your desired file has been renamed')
##    def open_folder():
##        folder = fd.askdirectory(title="Select Folder to open")
##        os.startfile(folder)
##    def delete_folder():
##        folder_to_delete = fd.askdirectory(title='Choose a folder to delete')
##        os.rmdir(folder_to_delete)
##        mb.showinfo("Folder Deleted", "Your desired folder has been deleted")
##    def move_folder():
##        folder_to_move = fd.askdirectory(title='Select the folder you want to move')
##        mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
##        destination = fd.askdirectory(title='Where to move the folder to')
##        try:
##            shutil.move(folder_to_move, destination)
##            mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
##        except:
##            mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')
##    def list_files_in_folder():
##        i = 0
##        folder = fd.askdirectory(title='Select the folder whose files you want to list')
##        files = os.listdir(os.path.abspath(folder))
##        list_files_wn = Toplevel(r)
##        list_files_wn.title(f'Files in {folder}')
##        list_files_wn.geometry('250x250')
##        list_files_wn.resizable(0, 0)
##        listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Georgia", 10))
##        listbox.grid(rowspan=5, column=1, row=1)
##        scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
##        scrollbar.grid(row=0, rowspan=4, column=2)
##        listbox.config(yscrollcommand=scrollbar.set)
##        while i < len(files):
##            listbox.insert(END, files[i])
##            i += 1
        # Defining the variables
##title = 'File Manager'
##background = 'Light Green'
##button_font = ("Times New Roman", 13)
##button_background = 'Turquoise'
### Initializing the window
##r = Tk()
##r.title(title)
##r.geometry('220x400')
##r.resizable(0, 0)
##r.config(bg=background)
# Creating and placing the components in the window
##Label(r, text=" ", font=("Ariel Black", 15), bg=background, wraplength=250).grid(column=0, row=1)
##Label(r, text=title, font=("Ariel Black", 15), bg=background, wraplength=250).grid(column=1, row=1)
##Button(r, text='Open a file', width=20, font=button_font, bg=button_background, command=open_file).grid(column=1, row=2)
##Button(r, text='Copy a file', width=20, font=button_font, bg=button_background, command=copy_file).grid(column=1, row=3)
##Button(r, text='Rename a file', width=20, font=button_font, bg=button_background, command=rename_file).grid(column=1, row=4)
##Button(r, text='Delete a file', width=20, font=button_font, bg=button_background, command=delete_file).grid(column=1, row=5)
##Button(r, text='Open a folder', width=20, font=button_font, bg=button_background, command=open_folder).grid(column=1, row=6)
##Button(r, text='Delete a folder', width=20, font=button_font, bg=button_background, command=delete_folder).grid(column=1, row=6)
##Button(r, text='Move a folder', width=20, font=button_font, bg=button_background, command=move_folder).grid(column=1, row=7)
##Button(r, text='List all files in a folder', width=20, font=button_font, bg=button_background,
##command=list_files_in_folder).grid(column=1, row=9)
# Finalizing the window
##r.update()
##r.mainloop()


r.mainloop()
   



