import os
import fnmatch
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Basic knowledge base for standard Python library functions
KNOWLEDGE_BASE = {
    "print": "Outputs text to the console.",
    "len": "Returns the number of items in a container.",
    "sum": "Returns the sum of all items in an iterable.",
    "max": "Returns the largest item in an iterable or two or more arguments.",
    "min": "Returns the smallest item in an iterable or two or more arguments.",
    "range": "Generates a sequence of numbers from start to stop (exclusive).",
    "sorted": "Returns a new sorted list from the items in an iterable.",
    "open": "Opens a file and returns a file object.",
    "input": "Reads a line of input from the user.",
    "map": "Applies a function to all items in an input list.",
    "filter": "Constructs an iterator from items in iterable for which function returns true.",
    "set": "Creates a set object, which is an unordered collection of unique items.",
    "frozenset": "Returns an immutable version of a set.",
    "list": "Creates a list object, a mutable sequence.",
    "tuple": "Creates a tuple object, an immutable sequence.",
    "dict": "Creates a dictionary object, a collection of key-value pairs.",
    "str": "Creates a string object or converts an object to a string.",
    "int": "Converts an object to an integer or returns an integer object.",
    "float": "Converts an object to a floating-point number or returns a float object.",
    "complex": "Creates a complex number or converts an object to a complex number.",
    "bool": "Returns a Boolean value, True or False.",
    "bin": "Converts an integer to its binary representation as a string.",
    "hex": "Converts an integer to its hexadecimal representation as a string.",
    "oct": "Converts an integer to its octal representation as a string.",
    "id": "Returns the unique identifier of an object.",
    "hash": "Returns the hash value of an object, if it has one.",
    "format": "Formats a value with a specified format string.",
    "chr": "Returns the character corresponding to an ASCII value.",
    "ord": "Returns the ASCII value corresponding to a character.",
    "repr": "Returns a string containing a printable representation of an object.",
    "globals": "Returns a dictionary of the current global symbol table.",
    "locals": "Returns a dictionary of the current local symbol table.",
    "memoryview": "Returns a memory view object of a given object.",
    "staticmethod": "Converts a method into a static method.",
    "classmethod": "Converts a method into a class method.",
    "property": "Returns a property object, which can define getters, setters, and deleters.",    
    "zip" : "Combines two or more iterables into tuples.",
    "any":  "Returns True if any element of an iterable is true.",
    "all": "Returns True if all elements of an iterable are true.",
    "enumerate": "Returns an enumerate object that adds a counter to an iterable.",
    "abs": "Returns the absolute value of a number.",
    "round": "Rounds a number to a specified number of decimal places.",
    "isinstance": "Checks if an object is an instance or subclass of a class.",
    "type": "Returns the type of an object.",
    "dir": "Returns a list of valid attributes for an object.",
    "help": "Displays help information for an object.",
    "eval": "Parses and evaluates a Python expression as a string.",
    "exec": "Executes dynamically generated Python code.",
    "reversed": "Returns a reverse iterator for a sequence.",
    "pow": "Returns the result of a number raised to a power.",
    "divmod": "Returns a tuple containing the quotient and remainder of a division."
}


EXCLUDED_EXTENSIONS = {'.pyc', '.log', '.txt', '.png', '.jpg', '.mp3', '.bmp'}

class CodeSnippetExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Snippet Extractor")

        # Directory selection widgets
        self.dir_label = tk.Label(root, text="Directory:")
        self.dir_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.dir_entry = tk.Entry(root, width=40)
        self.dir_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.recursive_var = tk.BooleanVar(value=True)
        self.recursive_check = tk.Checkbutton(root, text="Recursive", variable=self.recursive_var)
        self.recursive_check.grid(row=1, column=0, columnspan=3, pady=5)

        # Button to start extraction
        self.extract_button = tk.Button(root, text="Extract Snippets", command=self.extract_snippets)
        self.extract_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Text box to display snippets
        self.snippets_text = tk.Text(root, wrap="word", height=20, width=80)
        self.snippets_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Save and Clear buttons
        self.save_button = tk.Button(root, text="Save Snippets", command=self.save_snippets)
        self.save_button.grid(row=4, column=0, pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_snippets)
        self.clear_button.grid(row=4, column=2, pady=10)

        # Button to add to the knowledge base
        self.add_knowledge_button = tk.Button(root, text="Add to Knowledge Base", command=self.add_to_knowledge_base)
        self.add_knowledge_button.grid(row=5, column=0, columnspan=3, pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)

    def extract_snippets(self):
        directory = self.dir_entry.get()
        if not directory:
            messagebox.showwarning("No Directory Selected", "Please select a directory first.")
            return

        snippets = self.get_code_snippets(directory, self.recursive_var.get())
        self.snippets_text.delete("1.0", tk.END)
        self.snippets_text.insert(tk.END, "\n".join(snippets))

    def get_code_snippets(self, directory, recursive):
        snippets = []

        file_paths = [
            os.path.join(root, filename)
            for root, _, files in os.walk(directory)
            for filename in fnmatch.filter(files, "*.py")
            if not filename.endswith(tuple(EXCLUDED_EXTENSIONS))
        ] if recursive else [
            os.path.join(directory, filename)
            for filename in os.listdir(directory)
            if fnmatch.fnmatch(filename, "*.py") and not filename.endswith(tuple(EXCLUDED_EXTENSIONS))
        ]

        for filepath in file_paths:
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    functions = re.findall(r"(?:#.*\n)?def\s+(\w+)\(.*?\):\n((?: {4}.*\n)+)", content)
                    for func_name, code_block in functions:
                        description = KNOWLEDGE_BASE.get(func_name, "No description available")
                        snippet_text = f"File: {filepath}\nFunction: {func_name}\nDescription: {description}\nCode:\n{code_block.strip()}\n{'-'*40}\n"
                        snippets.append(snippet_text)
            except (FileNotFoundError, PermissionError):
                print(f"Cannot access: {filepath}")

        if not snippets:
            messagebox.showinfo("No Snippets Found", "No functions found in the selected directory.")

        return snippets

    def save_snippets(self):
        snippets = self.snippets_text.get("1.0", tk.END).strip()
        if not snippets:
            messagebox.showwarning("No Snippets", "No snippets to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(snippets)
            messagebox.showinfo("Saved", f"Snippets saved to {file_path}")

    def clear_snippets(self):
        self.snippets_text.delete("1.0", tk.END)

    def add_to_knowledge_base(self):
        func_name = tk.simpledialog.askstring("Function Name", "Enter the function name:")
        description = tk.simpledialog.askstring("Description", f"Enter the description for {func_name}:")
        if func_name and description:
            KNOWLEDGE_BASE[func_name] = description
            messagebox.showinfo("Knowledge Base Updated", f"Added {func_name} to knowledge base.")

# Main application
root = tk.Tk()
app = CodeSnippetExtractorApp(root)
root.mainloop()
