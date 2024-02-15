import csv
import os
import hashlib
import tkinter as tk
from tkinter import messagebox

def hash_password(password):
    # Hash the password before storing it
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the user already exists
    if os.path.exists("users.csv"):
        with open("users.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    messagebox.showerror("Error", "Username already exists. Please choose a different one.")
                    return

    # Hash the password before storing
    hashed_password = hash_password(password)
    
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])
    messagebox.showinfo("Success", "Sign up successful!")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if not os.path.exists("users.csv"):
        messagebox.showerror("Error", "No users found. Please sign up first.")
        return False
    
    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == hash_password(password):
                messagebox.showinfo("Success", "Login successful!")
                return True
    messagebox.showerror("Error", "Invalid username or password. Please try again.")
    return False

def main():
    global username_entry, password_entry

    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("500x500")

    title_label = tk.Label(root, text="Welcome to the Inventory Management System", font=("Helvetica", 16))
    title_label.pack(pady=20)

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    sign_up_button = tk.Button(root, text="Sign Up", command=sign_up)
    sign_up_button.pack(pady=5)

    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
