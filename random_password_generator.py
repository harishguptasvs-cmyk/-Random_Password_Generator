import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += "!@#$%^&*"

    if characters == "":
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

root.mainloop()
