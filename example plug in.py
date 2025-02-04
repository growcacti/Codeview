from plugin_base import PluginBase
import tkinter as tk

class WordCountPlugin(PluginBase):
    def execute(self):
        text = self.editor.get_current_textwidget().get(1.0, "end-1c")
        word_count = len(text.split())
        tk.messagebox.showinfo("Word Count", f"Word count: {word_count}")

