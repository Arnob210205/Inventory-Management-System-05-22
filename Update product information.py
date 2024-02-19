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
