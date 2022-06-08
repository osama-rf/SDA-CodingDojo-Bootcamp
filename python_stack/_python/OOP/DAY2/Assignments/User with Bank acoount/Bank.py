class Bank_account():
    def __init__(self, int_rate= 0.01, balacnce= 0):
        self.int_rate = int_rate
        self.balance = balacnce
    
    def deposit(self, amount):
        self.balance += amount
        print(f"You have successfully deposit ${amount}.")
        return amount

    def withdraw(self, amount):
        if (self.balance < amount):
            print(f"Insufficient funds: Charging a $5 fee and deduct $5 ")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Hi your account amount is {self.balance}")
        return self

    def yield_interest(self):
        interest = round(self.balance * self.int_rate)
        if(self.balance > 0):
            print(f"Your balance has increased by ${interest} couse by interest yield")
        else:
            print(f"Try to deposit to get interest next time, Thank You")
            return self
