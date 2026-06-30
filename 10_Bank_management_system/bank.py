from account import Account

class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account


        return None      
    
    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return True 

        return False    
    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
            print("Money deposited successfully")

        else:
            print("Account not found")    
    
    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
            print("Withdrawal successfull")
        else:
            print("Account not found)")    

    def display_all_accounts(self):
        for accounts in self.accounts:
            accounts.display()

    def remove_account(self, account_number):
        account = self.find_account(account_number)
        if account:
         self.accounts.remove(account) 
         return True
        else:

            return False          
        