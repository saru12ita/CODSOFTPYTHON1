import tkinter as tk
import secrets
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        result_label.config(text="Invalid length")
        return
    
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(secrets.choice(characters) for _ in range(password_length))
    
    # Update the result label
    result_label.config(text=password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x250")
app.configure(bg="green")

# Create and configure widgets
title_label = tk.Label(app, text="Password Generator", fg="blue", bg="green", font=("Arial", 18, "bold"))
length_label = tk.Label(app, text="Password Length:", fg="red", bg="green", font=("Arial", 12))
length_entry = tk.Entry(app, font=("Arial", 14, "bold"), bg="pink")
generate_button = tk.Button(app, text="Generate Password", command=generate_password, fg="red", bg="green", font=("Arial", 14, "bold"))
result_label = tk.Label(app, text="", fg="blue", bg="green", font=("Arial", 14, "bold"))

# Place widgets in the window
title_label.pack(pady=10)
length_label.pack()
length_entry.pack(pady=5)
generate_button.pack(pady=10)
result_label.pack()

# Start the application
app.mainloop()
