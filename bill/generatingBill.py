import json
import os

orderFile = "data/order.json"

def loadOrder():
    if not os.path.exists(orderFile):
        return []
    
    with open(orderFile) as file:
        return json.load(file)

def generatingBill():

    order = loadOrder()

    if not order:
        print("No order to bill.")
        return
    
    orderId = int(input("Enter order Id: "))
    order = next((o for o in order if o['order_id'] == orderId), None)

    if not order:
        print("order not found!")
        return
    
    subTotal = order["total"]
    taxRate = 0.05
    tax = subTotal * taxRate

    discount = 0

    applyDiscount = input("Apply discount? (y/n): ").lower()

    if applyDiscount == "y":
        discount = float(input("Enter discount amount: "))

    grandTotal = subTotal + tax - discount

    print("\n------ Customer bill ------")
    print(f"Customer : {order["customer_name"]}")
    print(f"Order ID: {order['order_id']}")
    print("-" * 30)
    for item in order['items']:
        line_total = item["price"] * item["quantity"]
        print(f"{item["name"]} x {item["quantity"]} = {line_total}")
    print("-" * 30)
    print(f"Subtotal: {subTotal:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Discount: -{discount:.2f}")
    print(f"Grand Total: {grandTotal:.2f}")
    print("-" * 30)