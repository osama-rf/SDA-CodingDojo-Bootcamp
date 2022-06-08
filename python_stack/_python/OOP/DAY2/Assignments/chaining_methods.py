class User():

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, deposit):
        self.balance += deposit
        return self

    def make_withdrawal(self, withdrawal):
        if(withdrawal > self.balance):
            print("Sorry you don't have enough money")
        else:
            self.balance -= withdrawal
            return self

    def display_user_balance(self):
        print(f"Hi {self.name} your account amount is {self.balance}")

    def transfer_money(self, target, tranafer):
        if(tranafer > self.balance):
            print("Sorry Yor Money isn't enough")
        else:
            self.balance -= tranafer
            target.balance += tranafer
            return self


user1 = User("Osama", 1000)

user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()