class Account:
    
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name 
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount 


    def withdraw(self, amount):
        if amount <= self.balance:
         self.balance -= amount 
        else:
            print("Insufficient balance")

    def display(self):
        print("----Account details----")
        print(f"Account number : {self.account_number}")
        print(f"Name : {self.name}")
        print(f"Available Balance: {self.balance}")
    








