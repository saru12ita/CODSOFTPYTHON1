import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact_list.insert(tk.END, f"{name}: {phone}")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        clear_entries()
    else:
        messagebox.showwarning("Error", "Name and Phone fields are required!")

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, data in contacts.items():
        contact_list.insert(tk.END, f"{name}: {data['phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for name, data in contacts.items():
        if search_term.lower() in name.lower() or search_term in data['phone']:
            contact_list.insert(tk.END, f"{name}: {data['phone']}")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE).split(":")[0]
    new_phone = new_phone_entry.get()
    new_email = new_email_entry.get()
    new_address = new_address_entry.get()

    if selected_contact in contacts:
        contacts[selected_contact]["phone"] = new_phone
        contacts[selected_contact]["email"] = new_email
        contacts[selected_contact]["address"] = new_address
        view_contacts()

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE).split(":")[0]
    if selected_contact in contacts:
        del contacts[selected_contact]
        view_contacts()

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("800x600")
root.configure(bg="red")

# Create a frame for contact information
contact_info_frame = tk.Frame(root, bg="red")
contact_info_frame.pack(pady=10)

# Labels and Entry Fields for Contact Information
name_label = tk.Label(contact_info_frame, text="Name:", bg="red", fg="pink", font=("bold", 25))
name_label.grid(row=0, column=0)
name_entry = tk.Entry(contact_info_frame, font=("bold", 25))
name_entry.grid(row=0, column=1)

phone_label = tk.Label(contact_info_frame, text="Phone:", bg="red", fg="pink", font=("bold", 25))
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(contact_info_frame, font=("bold", 25))
phone_entry.grid(row=1, column=1)

email_label = tk.Label(contact_info_frame, text="Email:", bg="red", fg="pink", font=("bold", 25))
email_label.grid(row=2, column=0)
email_entry = tk.Entry(contact_info_frame, font=("bold", 25))
email_entry.grid(row=2, column=1)

address_label = tk.Label(contact_info_frame, text="Address:", bg="red", fg="pink", font=("bold", 25))
address_label.grid(row=3, column=0)
address_entry = tk.Entry(contact_info_frame, font=("bold", 25))
address_entry.grid(row=3, column=1)

# Create buttons for adding, viewing, and searching contacts
add_button = tk.Button(contact_info_frame, text="Add Contact", command=add_contact, font=("bold", 20), bg="pink")
add_button.grid(row=4, column=0, columnspan=2, pady=10)

view_button = tk.Button(contact_info_frame, text="View Contacts", command=view_contacts, font=("bold", 20), bg="pink")
view_button.grid(row=4, column=2, columnspan=2, pady=10)

search_label = tk.Label(contact_info_frame, text="Search:", bg="red", fg="pink", font=("bold", 25))
search_label.grid(row=5, column=0)
search_entry = tk.Entry(contact_info_frame, font=("bold", 25))
search_entry.grid(row=5, column=1)

search_button = tk.Button(contact_info_frame, text="Search", command=search_contact, font=("bold", 20), bg="pink")
search_button.grid(row=5, column=2, columnspan=2, pady=10)

# Create a frame for displaying contacts
contact_list_frame = tk.Frame(root, bg="red")
contact_list_frame.pack(pady=10)

# Listbox for displaying contacts
contact_list = tk.Listbox(contact_list_frame, font=("bold", 20), bg="pink", selectbackground="red")
contact_list.pack()

# Create a frame for updating and deleting contacts
update_delete_frame = tk.Frame(root, bg="red")
update_delete_frame.pack(pady=10)

update_label = tk.Label(update_delete_frame, text="Update Contact:", bg="red", fg="pink", font=("bold", 25))
update_label.grid(row=0, column=0)

new_phone_label = tk.Label(update_delete_frame, text="New Phone:", bg="red", fg="pink", font=("bold", 20))
new_phone_label.grid(row=1, column=0)
new_phone_entry = tk.Entry(update_delete_frame, font=("bold", 20))
new_phone_entry.grid(row=1, column=1)

new_email_label = tk.Label(update_delete_frame, text="New Email:", bg="red", fg="pink", font=("bold", 20))
new_email_label.grid(row=2, column=0)
new_email_entry = tk.Entry(update_delete_frame, font=("bold", 20))
new_email_entry.grid(row=2, column=1)

new_address_label = tk.Label(update_delete_frame, text="New Address:", bg="red", fg="pink", font=("bold", 20))
new_address_label.grid(row=3, column=0)
new_address_entry = tk.Entry(update_delete_frame, font=("bold", 20))
new_address_entry.grid(row=3, column=1)

update_button = tk.Button(update_delete_frame, text="Update", command=update_contact, font=("bold", 20), bg="pink")
update_button.grid(row=4, column=0, columnspan=2, pady=10)

delete_button = tk.Button(update_delete_frame, text="Delete", command=delete_contact, font=("bold", 20), bg="pink")
delete_button.grid(row=4, column=2, columnspan=2, pady=10)

# Dictionary to store contact information
contacts = {}

root.mainloop()