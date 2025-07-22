import json

menuFile = "data/menu.json"

def loadMenu():
    with open(menuFile) as file:
        return json.load(file)

def saveMenu(menu):
    with open(menuFile, "w") as file:
        json.dump(menu, file, indent=4)

def displayMenu():
    menu = loadMenu()

    print("-------- Menu --------")

    for item in menu:
        print(f"{item["id"]}.item{item["name"]}-{item["price"]}")

def addMenuItem():
    menu = loadMenu()
    newId = max([item['id'] for item in menu], default=0)+1
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    menu.append({"id":newId, "name": name, "price":price})

    saveMenu(menu)
    print("Item add successfully!!")
    
def updateMenu():
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


