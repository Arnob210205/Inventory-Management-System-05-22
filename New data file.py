import tkinter as tk
from tkinter import messagebox

class InventoryManagementGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")

        # Initialize product database (for demonstration purposes)
        self.products = {'Apple': {'total': 50, 'sold': 0},
                         'Banana': {'total': 30, 'sold': 0},
                         'Orange': {'total': 40, 'sold': 0},
                         'Grape': {'total': 25, 'sold': 0}
                         'blueberry': {'total': 35, 'sold': 0},
                         'raspberry': {'total': 25, 'sold': 0 }
        }

        # Initialize GUI components
        self.label = tk.Label(master, text="Inventory Management System")
        self.label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

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

        self.sell_product_label = tk.Label(master, text="Sell Product:")
        self.sell_product_label.grid(row=4, column=0, padx=10, pady=5)
        self.sell_product_entry = tk.Entry(master)
        self.sell_product_entry.grid(row=4, column=1, padx=10, pady=5)

        self.sell_quantity_label = tk.Label(master, text="Sell Quantity:")
        self.sell_quantity_label.grid(row=5, column=0, padx=10, pady=5)
        self.sell_quantity_entry = tk.Entry(master)
        self.sell_quantity_entry.grid(row=5, column=1, padx=10, pady=5)

        self.sell_button = tk.Button(master, text="Sell", command=self.sell_product)
        self.sell_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

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
            self.products[product]['total'] += quantity
        else:
            self.products[product] = {'total': quantity, 'sold': 0}

        messagebox.showinfo("Success", f"Product '{product}' added successfully!")

    def sell_product(self):
        product = self.sell_product_entry.get().strip()
        quantity = self.sell_quantity_entry.get().strip()

        if not product:
            messagebox.showerror("Error", "Product name cannot be empty.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a positive integer.")
            return

        quantity = int(quantity)

        if product in self.products:
            if self.products[product]['total'] >= quantity:
                self.products[product]['total'] -= quantity
                self.products[product]['sold'] += quantity
                messagebox.showinfo("Success", f"{quantity} {product}(s) sold successfully!")
            else:
                messagebox.showerror("Error", f"Not enough {product} in stock.")
        else:
            messagebox.showerror("Error", f"Product '{product}' does not exist.")

    def view_inventory(self):
        inventory_window = tk.Toplevel(self.master)
        inventory_window.title("Inventory Levels")

        inventory_text = tk.Text(inventory_window, height=10, width=40)
        inventory_text.insert(tk.END, "Product\tTotal\tSold\tRemaining\n")
        for product, data in self.products.items():
            total = data['total']
            sold = data['sold']
            remaining = total - sold
            inventory_text.insert(tk.END, f"{product}\t{total}\t{sold}\t{remaining}\n")
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

