
import json

import getpass

def login():
    try:
        with open("data/user.json") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return None
    
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\nLogin successfully. Welcome {username}")
            return user
    
    print("\nInvalid credentials.")
    
    return None
         

