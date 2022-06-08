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


user1 = User("Osama", 100)
user2 = User("Anas", 500)
user3 = User("Faisal", 200)

# user1.make_deposit(20)
# user1.make_deposit(10)
# user1.make_deposit(50)
# user1.make_withdrawal(20)
# user1.display_user_balance()

# user2.make_deposit(50)
# user2.make_deposit(20)
# user2.make_withdrawal(90)
# user2.make_withdrawal(50)
# user2.display_user_balance()

user3.make_deposit(10)
user3.make_withdrawal(90)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.display_user_balance()


# user1.transfer_money(target=user3, tranafer= 50).display_user_balance()
# user3.display_user_balance()
