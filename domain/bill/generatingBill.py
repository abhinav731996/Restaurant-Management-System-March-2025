import json
import os

ORDER_FILE = "database/orders.json"  

def loadOrders():
    if not os.path.exists(ORDER_FILE):
        return []
    with open(ORDER_FILE) as file:
        return json.load(file)

def saveOrders(orders):
    with open(ORDER_FILE, "w") as file:
        json.dump(orders, file, indent=4)

def generatingBill():
    orders = loadOrders()
    pending_orders = [o for o in orders if o.get("status") != "paid"]

    if not pending_orders:
        print("No pending orders to bill.")
        return

    print("\n------ Pending Orders ------")
    for o in pending_orders:
        print(f"Order ID: {o['order_id']}, Customer: {o['customer_name']}, Amount: ₹{o['total']}")

    try:
        orderId = int(input("\nEnter Order ID to generate bill: "))
    except ValueError:
        print("Invalid Order ID.")
        return

    selected_order = next((o for o in orders if o['order_id'] == orderId and o.get("status") != "paid"), None)

    if not selected_order:
        print("Order not found or already paid.")
        return

    subTotal = selected_order["total"]
    taxRate = 0.05
    tax = subTotal * taxRate
    discount = 0

    applyDiscount = input("Apply discount? (y/n): ").lower()
    if applyDiscount == "y":
        try:
            discount = float(input("Enter discount amount: "))
        except ValueError:
            print("Invalid discount input. No discount applied.")
            discount = 0

    grandTotal = subTotal + tax - discount

    print("\n====== CUSTOMER BILL ======")
    print(f"Customer : {selected_order['customer_name']}")
    print(f"Order ID : {selected_order['order_id']}")
    print("-" * 30)
    for item in selected_order['items']:
        line_total = item["price"] * item["quantity"]
        print(f"{item['name']} x {item['quantity']} = ₹{line_total}")
    print("-" * 30)
    print(f"Subtotal     : ₹{subTotal:.2f}")
    print(f"Tax (5%)     : ₹{tax:.2f}")
    print(f"Discount     : -₹{discount:.2f}")
    print(f"Grand Total  : ₹{grandTotal:.2f}")
    print("-" * 30)

    confirm = input("Mark order as paid? (y/n): ").lower()
    if confirm == "y":
        selected_order["status"] = "paid"
        saveOrders(orders)
        print("Payment completed. Order marked as paid.")
    else:
        print("Order not marked as paid.")
