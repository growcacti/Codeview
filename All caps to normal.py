import tkinter as tk
from tkinter import scrolledtext

def correct_sentences():
    text = text_widget.get("1.0", tk.END)  # Get all text from the Text widget
    corrected_text = text.capitalize()  # Capitalize the first letter of each sentence
    sentences = corrected_text.split(". ")  # Split into sentences based on periods
    corrected_text = ". ".join(sentence.capitalize() for sentence in sentences)  # Capitalize each sentence
    text_widget.delete("1.0", tk.END)  # Clear the Text widget
    text_widget.insert(tk.END, corrected_text)  # Insert corrected text

# Create the main window
root = tk.Tk()
root.title("Sentence Capitalizer")

# Create a Text widget
text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_widget.pack(padx=10, pady=10)

# Create a Button to correct the sentences
correct_button = tk.Button(root, text="Correct Sentences", command=correct_sentences)
correct_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
