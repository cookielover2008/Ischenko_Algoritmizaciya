import tkinter as tk
from tkinter import ttk

def send_message():
    print(f"Name: {name_entry.get()}")
    print(f"Email: {email_entry.get()}")
    print(f"Message: {message_entry.get('1.0', tk.END)}")
    print(f"Subject: {subject_var.get()}")

root = tk.Tk()
root.title("Contact Form")
root.geometry("300x400")
root.config(bg="#ddd")

title_label = ttk.Label(root, text="Contact Form", font=('Arial', 16))
title_label.pack(pady=(10, 0))

subtitle_label = ttk.Label(root, text="Please fill all entries.", font=('Arial', 10))
subtitle_label.pack(pady=(0, 10))

name_label = ttk.Label(root, text="Name:")
name_label.pack(anchor='w', padx=10)

name_entry = ttk.Entry(root)
name_entry.pack(fill='x', padx=10)

email_label = ttk.Label(root, text="Email:")
email_label.pack(anchor='w', padx=10, pady=(10, 0))

email_entry = ttk.Entry(root)
email_entry.pack(fill='x', padx=10)

message_label = ttk.Label(root, text="Message:")
message_label.pack(anchor='w', padx=10, pady=(10, 0))

message_entry = tk.Text(root, height=5)
message_entry.pack(fill='x', padx=10)

subject_label = ttk.Label(root, text="Subject:")
subject_label.pack(anchor='w', padx=10, pady=(10, 0))

subject_var = tk.StringVar(value="Product Inquiry")
subject_combobox = ttk.Combobox(root, textvariable=subject_var)
subject_combobox['values'] = ("Product Inquiry", "Support", "Feedback")
subject_combobox.pack(fill='x', padx=10)

send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack(pady=20)

root.mainloop()
