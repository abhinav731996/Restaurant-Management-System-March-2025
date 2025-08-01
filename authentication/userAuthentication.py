
import json
import pwinput

Userfile = "database/user.json"
class Login:

    def __init__(self):
        pass

    def authenticateUser(self):
        
        username = input("Username: ")
        password = pwinput.pwinput(prompt="Password: ", mask="*")

        with open (Userfile, "r") as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"\nLogin successfully. Welcome {username}!")
                return user
        
        print("\nInvalid credentials.")
        
        return None
            

