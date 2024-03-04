import tkinter as tk

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
