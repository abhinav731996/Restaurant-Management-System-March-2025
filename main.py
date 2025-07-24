from authentication.userAuthentication import login
from menu.menuManagement import adminMenu
from order.orderProcessing import staffMenu

def menu():
    print("---------- Restaurent managemnet ----------")
     
    user = login()

    if user:
        if user["role"] == "admin":
            adminMenu()
        elif user["role"] == "staff":
            staffMenu()

        else:
            print("Invalid role!!")

    else:
        print("Login fail")


menu()
