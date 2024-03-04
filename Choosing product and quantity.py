import tkinter as tk

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
