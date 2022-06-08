from Bank import Bank_account

class User():

    def __init__(self, name):
        self.name = name
        self.account = {"Personal Account":Bank_account(0.01, 100)}
        return self

    def make_deposit(self, amount, bank_account = "personal account"):
        self.account[bank_account].deposit(amount)
        return self

    def make_withdrawal(self,  amount, bank_account = "personal account"):
        self.account[bank_account].withdraw(amount)
        print("Sorry you don't have enough money")
        return self

    def display_user_balance(self):
        print(f"Hi {self.name} your account amount is {self.account}")
        return self


user1 = User("Osama")

user1.make_deposit(20)
user1.make_deposit(10)
user1.make_deposit(50)
user1.make_withdrawal(20)
user1.display_user_balance()
