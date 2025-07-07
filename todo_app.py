import tkinter as tk
from tkinter import messagebox, filedialog

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, 'w') as f:
            for task in tasks:
                f.write(task + "\n")

def load_tasks():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        listbox.delete(0, tk.END)
        with open(file, 'r') as f:
            for task in f:
                listbox.insert(tk.END, task.strip())

# Main UI
root = tk.Tk()
root.title("Simple To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task)
remove_button.pack()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack()

root.mainloop()