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
