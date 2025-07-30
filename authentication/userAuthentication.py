
import json
import getpass

Userfile = "data/user.json"
class Login:

    def __init__(self):
        pass

    def authenticateUser(self):
        
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        with open (Userfile, "r") as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"\nLogin successfully. Welcome {username}!")
                return user
        
        print("\nInvalid credentials.")
        
        return None
            

