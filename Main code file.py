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

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Fruit Store Inventory")
        
        self.inventory = {'apple': 50, 'banana': 30, 'orange': 40, 'grape': 25}

        self.label = tk.Label(master, text="Welcome to the Fruit Store!")
        self.label.pack()

        self.fruit_label = tk.Label(master, text="Enter the name of the fruit:")
        self.fruit_label.pack()
        self.fruit_entry = tk.Entry(master)
        self.fruit_entry.pack()

        self.quantity_label = tk.Label(master, text="Enter the quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        self.purchase_button = tk.Button(master, text="Purchase", command=self.purchase)
        self.purchase_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def purchase(self):
        fruit = self.fruit_entry.get().lower()
        quantity = int(self.quantity_entry.get())

        if fruit in self.inventory and self.inventory[fruit] >= quantity:
            self.inventory[fruit] -= quantity
            self.result_label.config(text=f"You have successfully purchased {quantity} {fruit}(s)!")
        else:
            self.result_label.config(text="Sorry, we don't have enough of that fruit in stock or it's not available.")

def main():
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

class InventoryTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Tracker")
        
        self.inventory = {'Apple': 50, 'Banana': 30, 'Orange': 40, 'Grape': 25}

        self.label = tk.Label(master, text="Inventory Levels")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.inventory_text = tk.Text(master, height=10, width=30)
        self.display_inventory()
        self.inventory_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.refresh_button = tk.Button(master, text="Refresh", command=self.display_inventory)
        self.refresh_button.grid(row=2, column=0, padx=10, pady=10)

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, column=1, padx=10, pady=10)

    def display_inventory(self):
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(tk.END, "Fruit\t\tQuantity\n")
        for fruit, quantity in self.inventory.items():
            self.inventory_text.insert(tk.END, f"{fruit}\t\t{quantity}\n")

def main():
    root = tk.Tk()
    app = InventoryTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

class InventoryManagementGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")

        # Initialize product database (for demonstration purposes)
        self.products = {'Apple': 50, 'Banana': 30, 'Orange': 40, 'Grape': 25}

        # Initialize GUI components
        self.label = tk.Label(master, text="Inventory Management System")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.add_product_label = tk.Label(master, text="Add Product:")
        self.add_product_label.grid(row=1, column=0, padx=10, pady=5)
        self.add_product_entry = tk.Entry(master)
        self.add_product_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_quantity_label = tk.Label(master, text="Add Quantity:")
        self.add_quantity_label.grid(row=2, column=0, padx=10, pady=5)
        self.add_quantity_entry = tk.Entry(master)
        self.add_quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add", command=self.add_product)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.update_product_label = tk.Label(master, text="Update Product:")
        self.update_product_label.grid(row=4, column=0, padx=10, pady=5)
        self.update_product_entry = tk.Entry(master)
        self.update_product_entry.grid(row=4, column=1, padx=10, pady=5)

        self.update_quantity_label = tk.Label(master, text="Update Quantity:")
        self.update_quantity_label.grid(row=5, column=0, padx=10, pady=5)
        self.update_quantity_entry = tk.Entry(master)
        self.update_quantity_entry.grid(row=5, column=1, padx=10, pady=5)

        self.update_button = tk.Button(master, text="Update", command=self.update_product)
        self.update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.view_inventory_button = tk.Button(master, text="View Inventory", command=self.view_inventory)
        self.view_inventory_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def add_product(self):
        product = self.add_product_entry.get().strip()
        quantity = self.add_quantity_entry.get().strip()

        if not product:
            messagebox.showerror("Error", "Product name cannot be empty.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a positive integer.")
            return

        quantity = int(quantity)

        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

        messagebox.showinfo("Success", f"Product '{product}' added successfully!")

    def update_product(self):
        product = self.update_product_entry.get().strip()
        quantity = self.update_quantity_entry.get().strip()

        if not product:
            messagebox.showerror("Error", "Product name cannot be empty.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a positive integer.")
            return

        quantity = int(quantity)

        if product in self.products:
            self.products[product] = quantity
            messagebox.showinfo("Success", f"Quantity of product '{product}' updated successfully!")
        else:
            messagebox.showerror("Error", f"Product '{product}' does not exist.")

    def view_inventory(self):
        inventory_window = tk.Toplevel(self.master)
        inventory_window.title("Inventory Levels")

        inventory_text = tk.Text(inventory_window, height=10, width=30)
        inventory_text.insert(tk.END, "Product\t\tQuantity\n")
        for product, quantity in self.products.items():
            inventory_text.insert(tk.END, f"{product}\t\t{quantity}\n")
        inventory_text.pack(padx=10, pady=10)

        scrollbar = tk.Scrollbar(inventory_window, command=inventory_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        inventory_text.config(yscrollcommand=scrollbar.set)

def main():
    root = tk.Tk()
    app = InventoryManagementGUI(root)

if __name__ == "__main__":
    main()