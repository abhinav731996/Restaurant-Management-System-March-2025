import json
import os
from domain.menu.menu_manager import MenuManager  
from domain.bill.generatingBill import generatingBill  
from domain.table.table_booking import tableBookingMenu  
from datetime import datetime
from logs.log import error_logs

MENU_FILE = "database/menu.json"
ORDER_FILE = "database/orders.json"

class OrderManager:

    def __init__(self):
        if not os.path.exists(ORDER_FILE):
            with open(ORDER_FILE, "w") as f:
                json.dump([], f)

    def loadOrder(self):
        if not os.path.exists(ORDER_FILE):
            return []
        with open(ORDER_FILE) as file:
            return json.load(file)

    def saveOrder(self, orders):
        with open(ORDER_FILE, "w") as file:
            json.dump(orders, file, indent=4)

    from datetime import datetime

    def takeOrder(self):
        try:
            menu_mgr = MenuManager()
            menu = menu_mgr.loadMenu()
            if not menu:
                print("Menu is empty. Ask admin to add items.")
                return

            customerName = input("Enter customer name: ")
            orderItems = []
            total = 0

            menu_mgr.displayMenu()

            while True:
                itemName = input("\nEnter item name to add (or type 'done'): ").strip().lower()
                if itemName == "done":
                    break

                all_items = [item for items in menu.values() for item in items]
                matched_item = next((i for i in all_items if i["name"].lower() == itemName), None)

                if matched_item:
                    try:
                        qty = float(input(f"Enter quantity for {matched_item['name']}: "))
                        if qty <= 0 or qty > 50:
                            print("Quantity must be between 1 and 50.")
                            continue
                        item_total = matched_item["price"] * qty
                        total += item_total
                        orderItems.append({
                            "itemId": matched_item["id"],
                            "name": matched_item["name"],
                            "price": matched_item["price"],
                            "quantity": qty
                        })
                    except ValueError:
                        print("Invalid quantity input.")
                else:
                    print("Item not found.")

            if not orderItems:
                print("No items selected.")
                return

            # Date/time capture
            use_custom = input("Enter custom date/time? (y/n): ").strip().lower()
            if use_custom == "y":
                dt_input = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ").strip()
                try:
                    order_datetime = datetime.strptime(dt_input, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print("Invalid format. Using current date/time instead.")
                    order_datetime = datetime.now()
            else:
                order_datetime = datetime.now()

            all_orders = self.loadOrder()
            orderId = len(all_orders) + 1

            order = {
                "order_id": orderId,
                "customer_name": customerName,
                "items": orderItems,
                "total": total,
                "status": "pending",
                "datetime": order_datetime.strftime("%Y-%m-%d %H:%M:%S")
            }

            all_orders.append(order)
            self.saveOrder(all_orders)

            print(f"\nOrder placed successfully! Total amount = ₹{total}")
        except Exception as e:
            error_logs(e)



    def viewAllOrders(self):
        orders = self.loadOrder()
        if not orders:
            print("No orders found.")
            return

        print("\n------ All Orders ------")
        for order in orders:
            print(f"\nOrder ID: {order['order_id']}, Customer: {order['customer_name']}, Total: {order['total']}")
            for item in order["items"]:
                subtotal = item["price"] * item["quantity"]
                print(f"  {item['name']} x {item['quantity']} = {subtotal}")
            print("-" * 40)

    def staffMenu(self):
        while True:
            print("\n------ Staff Menu ------")
            print("1 - Take order")
            print("2 - View all orders")
            print("3 - Generate bill")
            print("4 - Table booking")
            print("5 - Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.takeOrder()
                elif choice == 2:
                    self.viewAllOrders()
                elif choice == 3:
                    generatingBill()
                elif choice == 4:
                    tableBookingMenu()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Enter a valid number.")
