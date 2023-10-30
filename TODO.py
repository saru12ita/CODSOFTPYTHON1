import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Function to add a new task
def add_task():
    task = entry.get()
    date = date_var.get()
    time = time_var.get()

    if task:
        task_with_datetime = f"{task} (Due: {date} at {time})"
        listbox.insert(tk.END, task_with_datetime)
        listbox.itemconfig(tk.END, {'fg': 'dark pink', 'font': ('Helvetica', 14, 'bold')})  # Set text color and style
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main application window
app = tk.Tk()
app.title("Colorful To-Do List")

# Set the background color to yellow
app.configure(bg="#FFFF00")

# Configure the window size
app.geometry("400x400")

# Create and configure the listbox
listbox = tk.Listbox(app, selectbackground="light blue", selectmode=tk.SINGLE, font=("Helvetica", 14), bg="#ffffff")
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create an entry widget for adding new tasks
entry = tk.Entry(app, font=("Helvetica", 14), bg="#ffffff")
entry.pack(pady=10, padx=10, fill=tk.X)

# Create labels for date and time
date_label = tk.Label(app, text="Due Date:", font=("Helvetica", 12), bg="#FFFF00")
time_label = tk.Label(app, text="Due Time:", font=("Helvetica", 12), bg="#FFFF00")
date_label.pack(pady=5)
time_label.pack(pady=5)

# Create date and time pickers
date_var = tk.StringVar()
time_var = tk.StringVar()
date_picker = ttk.Combobox(app, textvariable=date_var, values=["Today", "Tomorrow", "Custom"], font=("Helvetica", 12), state="readonly")
time_picker = ttk.Combobox(app, textvariable=time_var, values=["Morning", "Afternoon", "Evening", "Custom"], font=("Helvetica", 12), state="readonly")
date_picker.pack(pady=5)
time_picker.pack(pady=5)
date_picker.set("Today")
time_picker.set("Morning")

# Create buttons for adding and removing tasks
add_button = tk.Button(app, text="Add Task", command=add_task, font=("Helvetica", 14), bg="#4CAF50", fg="white")
remove_button = tk.Button(app, text="Remove Task", command=remove_task, font=("Helvetica", 14), bg="#FF0000", fg="white")
add_button.pack(pady=10, padx=10, fill=tk.BOTH)
remove_button.pack(pady=10, padx=10, fill=tk.BOTH)

# Start the main application loop
app.mainloop()
