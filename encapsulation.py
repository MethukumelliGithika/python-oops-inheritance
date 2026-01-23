class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")


# Object creation
atm = ATM("Githika", 5000)

atm.check_balance()
atm.deposit(2000)
atm.withdraw(3000)
atm.check_balance()

# This will cause error if uncommented
# print(atm.__balance)
