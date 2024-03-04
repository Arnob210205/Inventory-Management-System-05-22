import tkinter as tk
from tkinter import messagebox

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
    root.mainloop()

if __name__ == "__main__":
    main()

