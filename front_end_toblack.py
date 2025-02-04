import os
import tkinter as tk
from tkinter import filedialog, messagebox
from difflib import unified_diff
import mimetypes
import black  # Ensure Black is installed: pip install black


class DirectoryProcessorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Black Code Formatter Frontend")
        self.geometry("1000x600")

        # Input File/Directory
        self.label_input = tk.Label(self, text="Select File or Directory:")
        self.label_input.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_path = tk.Entry(self, width=50)
        self.entry_path.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.button_browse = tk.Button(self, text="Browse", command=self.browse)
        self.button_browse.grid(row=0, column=2, padx=10, pady=5)
        self.button_process = tk.Button(self, text="Process", command=self.process)
        self.button_process.grid(row=0, column=3, padx=10, pady=5)
        self.button_save = tk.Button(self, text="Save Processed File", command=self.save_file)
        self.button_save.grid(row=0, column=4, padx=10, pady=5)

        # Original Content
        self.label_original = tk.Label(self, text="Original Content:")
        self.label_original.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.text_original = tk.Text(self, wrap="word", height=30, width=60)
        self.text_original.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Processed Content
        self.label_processed = tk.Label(self, text="Processed (Formatted) Content:")
        self.label_processed.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.text_processed = tk.Text(self, wrap="word", height=30, width=60)
        self.text_processed.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky="w")

        # Variables
        self.current_file_path = None

    def browse(self):
        path = filedialog.askdirectory(title="Select a Directory") or filedialog.askopenfilename(title="Select a File")
        if path:
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, path)

    def process(self):
        path = self.entry_path.get()
        if not path:
            messagebox.showerror("Error", "Please select a valid file or directory.")
            return

        if os.path.isfile(path):
            self.process_file(path)
        elif os.path.isdir(path):
            self.process_directory(path)
        else:
            messagebox.showerror("Error", "Invalid path selected.")

    def process_file(self, file_path):
        if not self.is_python_file(file_path):
            messagebox.showinfo("Info", f"Skipped non-Python file: {file_path}")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.read()
            processed_content = self.format_code(original_content)
            self.current_file_path = file_path
            self.display_content(original_content, processed_content, file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error processing file {file_path}: {e}")

    def process_directory(self, dir_path):
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.process_file(file_path)

    def format_code(self, code):
        try:
            # Format code using Black
            return black.format_str(code, mode=black.Mode())
        except Exception as e:
            return f"Error formatting code: {e}"

    def display_content(self, original, processed, file_path):
        self.text_original.delete(1.0, tk.END)
        self.text_original.insert(tk.END, f"File: {file_path}\n\n{original}")

        self.text_processed.delete(1.0, tk.END)
        self.text_processed.insert(tk.END, f"File: {file_path}\n\n{processed}")

    def save_file(self):
        if not self.current_file_path:
            messagebox.showerror("Error", "No file processed to save.")
            return

        save_path = filedialog.asksaveasfilename(
            title="Save Processed File",
            initialfile=os.path.basename(self.current_file_path),
            defaultextension=".py",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )

        if save_path:
            try:
                processed_content = self.text_processed.get(1.0, tk.END).strip()
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(processed_content)
                messagebox.showinfo("Success", f"File saved to {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")

    def is_python_file(self, file_path):
        # Check if file is a Python file
        return file_path.endswith(".py")


if __name__ == "__main__":
    app = DirectoryProcessorApp()
    app.mainloop()
