# Hierarchical Inheritance Example

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def show_interest(self):
        print(f"Interest Rate: {self.interest_rate}%")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def show_overdraft(self):
        print(f"Overdraft Limit: {self.overdraft_limit}")


# Object creation
s1 = SavingsAccount("Githika", 5000, 5)
c1 = CurrentAccount("Anil", 10000, 2000)

s1.account_info()
s1.show_interest()

c1.account_info()
c1.show_overdraft()
