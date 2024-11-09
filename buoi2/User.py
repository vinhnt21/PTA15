"""
User
- Attributes: full_name, user_name, password
- Methods: login, change_password
"""
class User:
    def __init__(self, full_name, user_name, password):
        self.full_name = full_name
        self.user_name = user_name
        self.password = password

    def check_login(self, user_name, password):
        if self.user_name == user_name and self.password == password:
            print("Login successfully")
        else:
            print("Login failed")

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            print("Change password successfully")
        else:
            print("Old password is incorrect")
        

users = []


def register():
    full_name = input("Enter your full name: ")
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")

    user = User(full_name, user_name, password)
    users.append(user)
    print("Register successfully")


def show_user_list():
    print("User list")
    if len(users) == 0:
        print("No user")
    else:
        for user in users:
            print(f"Full name: {user.full_name}, User name: {user.user_name}")


def login(user_name, password):
    for user in users:
        user.check_login(user_name, password)


while True:
    print("1. Register")
    print("2. Show user list")
    print("3. Login")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        show_user_list()
    elif choice == "3":
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        login(user_name, password)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
