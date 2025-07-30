from authentication.signup import Signup
from authentication.userAuthentication import Login
from menu.menu_manager import MenuManager
from order.orderProcessing import OrderManager

def main():
    print("---------- Restaurant Management ----------")
    print("1. Sign Up")
    print("2. Login")
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
    else:
        print("Invalid option.")
        return

    
    if user["role"] == "admin":
        MenuManager().adminMenu()
    elif user["role"] == "staff":
        OrderManager().staffMenu()
    else:
        print("Unknown role!")

if __name__ == "__main__":
    main()
