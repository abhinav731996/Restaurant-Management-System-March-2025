from authentication.signup import Signup
from authentication.userAuthentication import Login
from domain.menu.menu_manager import MenuManager
from domain.order.orderProcessing import OrderManager

def main():
    print("---------- Restaurant Management ----------")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose option: ")

    user = None

    if choice == "1":
        Signup().createUser()
        return 
    elif choice == "2":
        user = Login().authenticateUser()
        if not user:
            return
        print(f"Access granted for {user['role']}")
    elif choice == "3":
        print("Exit...")
        return
    else:
        print("Invalid option.")
        return

    
    if user["role"] == "admin":
        MenuManager().adminMenu()
    elif user["role"] == "staff":
        OrderManager().staffMenu()
    else:
        print("Unknown role!")


main()
