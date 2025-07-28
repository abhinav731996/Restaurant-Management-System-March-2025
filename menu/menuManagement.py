import json
import os

menuFile = "data/menu.json"

def loadMenu():
    if not os.path.exists(menuFile):
        return []
    with open(menuFile) as file:
        return json.load(file)

def saveMenu(menu):
    with open(menuFile, "w") as file:
        json.dump(menu, file, indent=4)

def displayMenu():
    menu = loadMenu()

    print("-------- Menu --------")

    for category, item in menu.items():
        print(f"\n---- {category.capitalize()} ----")
        for item in item:
            print(f"{item['id']}. {item['name']} - {item['price']}")

def addMenuItem():
    menu = loadMenu()
    category = input("Enter category(beakfast/lunch/dinner): ")
    
    if category not in menu:
        print("Invalid category")
        return
    
    newId = int(max([item['id'] for cat_item in menu.values() for item in cat_item], default=0)+1)
    name = input("Enter item name: ")
    price = int(input("Enter price: "))
    menu.append({"id":newId, "name": name, "price":price})

    saveMenu(menu)
    print("Item add successfully!!")
    
def updateMenuItem():
    menu = loadMenu()
    displayMenu()
    IDtoUpdate = int(input("Enter ID to update: "))
    for item in menu:
        if item["id"] == IDtoUpdate:
            item["name"] = input("Enter new name: ")
            item["price"] = input("Enter new price: ")

            saveMenu(menu)
            print("Item update successfully!!")
            return
    print("Item not found.")

def deleteMenuItem():
    menu = loadMenu()
    displayMenu()
    IDtoDelete = int(input("enter ID to delete: "))
    newMenu = [item for item in menu if item["id"] != IDtoDelete]
    if len(newMenu) != len(menu):
        saveMenu(newMenu)
        print("Item delete successfully!! ")
    else:
        print("Item not found.")

def adminMenu():
    while True:
        print("\n------ Admin Menu -------")
        print("1 - View menu")
        print("2 - Add menu item")
        print("3 - Update menu item")
        print("4 - Delete menu item")
        print("5 - Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            displayMenu()
        elif choice == 2:
            addMenuItem()
        elif choice == 3:
            updateMenuItem()
        elif choice == 4:
            deleteMenuItem()
        elif choice == 5:
            break
        else:
            print("Invalid choice, try again")
            

