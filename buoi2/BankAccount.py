"""
BankAccount
- Attributes:
    + account_number
    + account_name
    + balance
- Methods:
    + deposit(amount)
    + withdraw(amount)
    + transfer(amount, target_account)
    + display
"""


class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount} successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} successfully")
        else:
            print("Not enough money")

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transfer {amount} successfully")
        else:
            print("Not enough money")

    def display(self):
        print(
            f"Blance: {self.balance}, account name: {self.account_name}, account number: {self.account_number}"
        )


acc1 = BankAccount("123", "Tran Van A", 100)
acc2 = BankAccount("124", "Tran Van B", 200)

acc1.display()
acc2.display()
acc2.transfer(50, acc1)
acc1.display()
acc2.display()
