import json 
import os 

from datetime import datetime

bookingFile  = "data/booking.json"

TIME_SLOTS = ["12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]


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
    
    bookingDate = input("Enter date to view bookings (YYYY-MM-DD): ")

    filteredBooking = [b for b in booking if b.get("bookingDate") == bookingDate]

    if not filteredBooking:
        print(f"No bookings found on {bookingDate}")
        return
    
    print("\n------ All table booking -------")
    
    for b in booking:
        print(f"Table {b["tableNo"]} | {b['customerName']} | {b["timeSlot"]}") 


def bookTable():

    booking = loadBooking()

    allTable = list(range(1,11))

    bookingDate = input("Enter booking date(YYYY-MM-DD): ")

    print("Available time slots: ", TIME_SLOTS)

    timeSlot = input("Enter time slot(HH:MM): ")
    if timeSlot not in TIME_SLOTS:
        print("Invalid time slot.")
        return
    

    bookedTable = [
        b["tableNo"] for b in booking
        if b["timeSlot"] == timeSlot and b["bookingDate"] == bookingDate
    ]

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
        "timeSlot": timeSlot,
        "dateTime": dateTime,
        "bookingDate": bookingDate
    })

    saveBooking(booking)
    print(f"Table{tableNo} booked for{customerName} on {bookingDate} at {timeSlot}")


def cancelBooking():

    booking = loadBooking()

    customerName = input("Enter customer name: ")
    tableNo = int(input("Enter table number to cancel: ")) 
    timeSlot = input("Enter time slot to cancel(HH:MM): ")
    bookingDate = input("Enter booking date (YYYY-MM-DD): ")


    updateBooking = [
        b for b in booking 
        if not (b["tableNo"] == tableNo and b["timeSlot"] == timeSlot and b["customerName"] == customerName and b["bookingDate"] == bookingDate)
    ]


    if len(updateBooking) == len(booking):
        print("no matching booking found.")
    else:
        saveBooking(updateBooking)
        print(f"booking for table{tableNo} on {bookingDate} at {timeSlot} cancelled.")



def tableBookingMenu():

    while True:
        print("\n--- Table Booking ---")
        print("1. Book a Table")
        print("2. View All Bookings")
        print("3. Cancel booking")
        print("4. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            bookTable()
        elif choice == '2':
            viewAllBooking()
        elif choice == '3':
            cancelBooking()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")