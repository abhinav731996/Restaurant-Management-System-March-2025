def dashboard(name):
    print(f"Welcome: {name}")

def getData():
    return [
        {"username": "admin", "password": "admin123", "role": "admin"},
        {"username": "staff", "password": "staff123", "role": "staff"}
    ]

userName = input("Enter username: ")
password = input("Enter password: ")

data = getData()
flag = 0

for user in data:
    if userName == user["username"] and password == user["password"]:
        dashboard(user["username"])
        flag = 1
        break

if flag == 0:
    print("Invalid credentials. Try again.")
