import json 
import os 

from datetime import datetime

bookingFile  = "data/booking.json"




def loadBooking():
    if not os.path.exists(bookingFile):
        return
    with open(bookingFile) as f:
        return json.load(f)
    
def saveBooking(booking):
    with open(bookingFile, "w") as f:
        json.dump(booking, f, indent=4)

def viewAllBooking():
    booking = loadBooking()
    if not booking:
        print("No booking yet")
        return
    
    print("\n------ All table bookin -------")
    
    for b in booking:
        print(f"Table {b["tableNo"]} | {b['customerName']} | {b["dateTime"]}") 


def bookTable():

    booking = loadBooking()

    allTable = list(range(1,11))
   

    bookedTable = [b["tableNo"] for b in booking]

    availableTable = [t for t in allTable if t not in bookedTable]

    if not availableTable:
        print("No table available.")
        return

    print("Availabe table", availableTable)
    customerName = input("Enter coustomer name: ")
    tableNo = int(input("Enter table number to book: "))

    if tableNo not in availableTable:
        print("Table already booked or invalid!!")
        return
    
    dateTime = datetime.now().strftime("%Y-%m-%d %H:%M")

    booking.append({
        "tableNo" : tableNo,
        "customerName" : customerName,
        "dateTime" : dateTime
    })

    saveBooking(booking)
    print(f"Table{tableNo} booked for{customerName}")


def tableBookingMenu():

    while True:
        print("\n--- Table Booking ---")
        print("1. Book a Table")
        print("2. View All Bookings")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            bookTable()
        elif choice == '2':
            viewAllBooking()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")