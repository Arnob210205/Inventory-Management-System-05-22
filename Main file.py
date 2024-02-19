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

    import tkinter as tk
from tkinter import messagebox

class InventoryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        
        self.products = {
            "Mango": 0,
            "Banana": 0,
            "Pineapple": 0,
            "Jackfruit": 0,
            "Blueberry": 0,
            "Raspberry": 0
        }
        
        self.create_widgets()

    def create_widgets(self):
        self.product_label = tk.Label(self.master, text="Select Product:")
        self.product_label.grid(row=0, column=0, padx=10, pady=5)

        self.product_var = tk.StringVar()
        self.product_var.set("Mango")
        self.product_dropdown = tk.OptionMenu(self.master, self.product_var, *self.products.keys())
        self.product_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.quantity_label = tk.Label(self.master, text="Enter Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=5)

        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.master, text="Add Product", command=self.add_product)
        self.add_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def add_product(self):
        product = self.product_var.get()
        quantity = self.quantity_entry.get()
        if quantity.isdigit():
            self.products[product] += int(quantity)
            messagebox.showinfo("Success", f"{quantity} {product}(s) added to inventory.")
        else:
            messagebox.showerror("Error", "Please enter a valid quantity.")

def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    import tkinter as tk

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Inventory Management System")

        self.label = tk.Label(master, text="Update Product Information")
        self.label.pack()

        self.product_label = tk.Label(master, text="Select Product:")
        self.product_label.pack()

        self.product_options = ["Mango", "Banana", "Pineapple", "Jackfruit", "Blueberry", "Raspberry"]
        self.product_var = tk.StringVar(master)
        self.product_var.set(self.product_options[0])

        self.product_menu = tk.OptionMenu(master, self.product_var, *self.product_options)
        self.product_menu.pack()

        self.quantity_label = tk.Label(master, text="Enter Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        self.update_button = tk.Button(master, text="Update", command=self.update_inventory)
        self.update_button.pack()

    def update_inventory(self):
        product = self.product_var.get()
        quantity = self.quantity_entry.get()

        print(f"Updating inventory for {product}: {quantity} units")

        self.quantity_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = InventoryGUI(root)
    root.mainloop()