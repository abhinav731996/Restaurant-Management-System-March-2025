import json
import os

menuFile = "data/menu.json"

class MenuManager:

    def __init__(self):
        if not os.path.exists(menuFile):
            with open(menuFile, "w") as f:
                json.dump({
                    "breakfast": [], "lunch": [], "dinner": [],
                    "southIndian": [], "chinese": [],
                    "drinks": [], "desserts": [], "snacks": []
                }, f, indent=4)

    def loadMenu(self):
        with open(menuFile, "r") as file:
            return json.load(file)

    def saveMenu(self, menu):
        with open(menuFile, "w") as file:
            json.dump(menu, file, indent=4)

    def displayMenu(self):
        menu = self.loadMenu()
        print("-------- Menu --------")
        for category, items in menu.items():
            print(f"\n---- {category.capitalize()} ----")
            for item in items:
                print(f"{item['id']}. {item['name']} - ₹{item['price']}")

    def addMenuItem(self):
        menu = self.loadMenu()
        category = input("Enter category (breakfast/lunch/dinner/southIndian/chinese/drinks/desserts/snacks): ").lower()
        
        if category not in menu:
            print("Invalid category.")
            return
        
        newId = int(max([item['id'] for cat in menu.values() for item in cat], default=0) + 1)
        name = input("Enter item name: ")
        price = int(input("Enter price: "))
        menu[category].append({"id": newId, "name": name, "price": price})

        self.saveMenu(menu)
        print("Item added successfully!")

    def updateMenuItem(self):
        menu = self.loadMenu()
        category = input("Enter category: ").lower()

        if category not in menu:
            print("Invalid category.")
            return

        self.displayMenu()
        try:
            IDtoUpdate = int(input("Enter ID to update: "))
            for item in menu[category]:
                if item["id"] == IDtoUpdate:
                    item["name"] = input("Enter new name: ") or item["name"]
                    item["price"] = int(input("Enter new price: ") or item["price"])
                    self.saveMenu(menu)
                    print("Item updated successfully!")
                    return
            print("Item not found.")
        except ValueError:
            print("Invalid input.")

    def deleteMenuItem(self):
        menu = self.loadMenu()
        category = input("Enter category: ").lower()

        if category not in menu:
            print("Invalid category.")
            return

        self.displayMenu()
        try:
            IDtoDelete = int(input("Enter ID to delete: "))
            original_len = len(menu[category])
            menu[category] = [item for item in menu[category] if item["id"] != IDtoDelete]

            if len(menu[category]) < original_len:
                self.saveMenu(menu)
                print("Item deleted successfully!")
            else:
                print("Item not found.")
        except ValueError:
            print("Invalid input.")

    def adminMenu(self):
        while True:
            print("\n------ Admin Menu -------")
            print("1 - View menu")
            print("2 - Add menu item")
            print("3 - Update menu item")
            print("4 - Delete menu item")
            print("5 - Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.displayMenu()
                elif choice == 2:
                    self.addMenuItem()
                elif choice == 3:
                    self.updateMenuItem()
                elif choice == 4:
                    self.deleteMenuItem()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a number.")
