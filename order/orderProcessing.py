import json
import os
from menu.menuManagement import displayMenu, loadMenu
from bill.generatingBill import generatingBill
from table.tableBooking import tableBookingMenu

orderFile = "data/order.json"

def loadOrder():
    if not os.path.exists(orderFile):
        return []
    with open(orderFile) as file:
        return json.load(file)

def saveOrder(order):
    with open(orderFile, "w") as file:
        json.dump(order, file, indent=4)

def takeOrder():
    menu = loadMenu()
    if not menu:
        print("Menu is empty. Ask admin to add Items")
        return
    customerName = input("Enter coustomer name: ")
    orderItem = []
    total = 0

    displayMenu()
    
    while True:
        itemId = input("Enter Id to add or done to finish: ")
        if itemId.lower() == "done":
            break

        all_items = [item for items in menu.values() for item in items] 
        item = next((i for i in all_items if str(i["id"]) == itemId), None)


        if item:
            qty = float(input(f"Enter quantity for {item['name']}: "))
            total += item["price"]*qty
            orderItem.append({
                "itemId": item["id"],
                "name": item["name"],
                "price": item["price"],
                "quantity": qty
            })
        else:
            print("Item not found.")

    if not orderItem:
        print("No item selected: ")
        return
    
    orderData = loadOrder()
    orderId = len(orderData)+1

    order = {
        "order_id": orderId,
        "customer_name": customerName,
        "items": orderItem,
        "total": total
    }
        
    orderData.append(order)
    saveOrder(orderData)

    print(f"\n Order placed successfully! Total amount = {total}")

def viewAllOrders():
    order = loadOrder()
    if not order:
        print("no order found")
        return

    print("\n------ All order ------")

    for order in order:
        print(f"\nOrder id: {order["order_id"]}, Customer: {order["customer_name"]}, Total: {order["total"]}")

        for item in order["items"]:
            print(f"  {item['name']} x {item['quantity']} = ₹{item['price'] * item['quantity']}")
        print("-" * 40)

def staffMenu():
    while True:
        print("\n------ Staff Menu ------")
        print("1 - Take order")
        print("2 - View all order")
        print("3 - Generate bill")
        print("4 - Table Booking")
        print("5 - Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            takeOrder()
        elif choice == 2:
            viewAllOrders()
        elif choice == 3:
            generatingBill()
        elif choice == 4:
            tableBookingMenu()
        elif choice == 5:
            break
        else:
            print("Invalid choice, try again!!")

        
