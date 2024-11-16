class User:
    def __init__(self, name, dob, email, password):
        self.name = name
        self.dob = dob
        self.email = email
        self.password = password

    def show_info(self):
        print(
            f"User: {self.name}, Date of Birth: {self.dob}, Email: {self.email}, Password: {self.password}"
        )


class Admin(User):
    def __init__(self, name, dob, email, password):
        super().__init__(name, dob, email, password)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin1 = Admin("Khanh", "01/01/1990", "a@a.com", "123456")
admin1.show_info()
