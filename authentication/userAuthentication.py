# def dashboard(name):
#     print(f"Welcome: {name}")

# def getData():
#     return [
#         {"username": "admin", "password": "admin123", "role": "admin"},
#         {"username": "staff", "password": "staff123", "role": "staff"}
#     ]

# userName = input("Enter username: ")
# password = input("Enter password: ")

# data = getData()
# flag = 0

# for user in data:
#     if userName == user["username"] and password == user["password"]:
#         dashboard(user["username"])
#         flag = 1
#         break

# if flag == 0:
#     print("Invalid credentials. Try again.")

# from menu.menuManagement import loadMenu
import json

def login():
    try:
        with open("data/user.json") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return None
    
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password and user["role"] == "admin" :
            print(f"\nLogin successfully. Welcome {username}")
            

            return user
    
    print("\nInvalid credentials.")
    
    return None

def regisNew():
    with open("data/user.json", "r") as files:
        content = files.read()
        data = json.loads(content)


    # listdata = []
    with open("data/user.json", "a") as files:
        file={}
        file['id']= input("Enter ID: ")
        file['password'] = input("Enter password: ")
        file["role"] = input("Enter role: ")

        inital=json.dumps(file,indent=4)
        data.append(dataf)
        

        files.write(dataf)
         

regisNew()
        
