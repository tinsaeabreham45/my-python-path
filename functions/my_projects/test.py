import random
import string
import pyperclip
import tkinter as tk


def random_password_generator(length):
    random_password = '@'
    random_password += ''.join(random.choice(string.ascii_uppercase))
    password_length = length
    random_password += ''.join(random.choices(string.ascii_lowercase + string.digits, k=password_length))
    return random_password


def generate_password():
    length = int(length_entry.get())
    password = random_password_generator(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Create tkinter window
root = tk.Tk()
root.title("Random Password Generator")

# Set initial window size
root.geometry("200x400")

# Length label and entry
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Password entry
password_entry = tk.Entry(root)
password_entry.pack()

root.mainloop()
