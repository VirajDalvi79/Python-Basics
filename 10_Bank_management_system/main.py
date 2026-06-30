from bank import Bank 
from account import Account


bank = Bank()
while True:
   try: 
    print("""---Bank Management System---
       1. Create account
       2. Deposit money
       3. Withdraw money 
       4. Check Balance
       5. Display all account
       6. Remove account
       7. Exit""")
    option = int(input("Select a correct option: "))
    if option == 1:
        number = int(input("Enter an account number: "))
        name = str(input("Enter the name of the account: "))
        balance = float(input("Enter the initial balance: "))
        acc = Account(number, name, balance)
        bank.add_account(acc)
        print("Account added successfully")


    elif option == 2:
            account_number = int(input("Enter account number: "))
            amount = int(input("Enter the amount: ")) 
            bank.deposit_money(account_number, amount )


    elif option == 3:
         account_number = int(input("Enter your account number: "))
         amount = int(input("Enter the amount: "))
         bank.withdraw_money(account_number, amount)


    elif option == 4:
         account_number = int(input("Enter your account number: "))
         account = bank.find_account(account_number)
         print(account.balance)


    elif option == 5:
              bank.display_all_accounts()


    elif option == 6:
     account_number = int(input("Enter the account number: "))
     if bank.remove_account(account_number):
        print("Account removed successfully.")
     else:
        print("Account not found.")   

    elif option == 7:
       print("Thank you for using Bank Management System.")
       break     


   except KeyboardInterrupt:
        print("Bye Bye")     
        break
   except ValueError:
        print("Unexpected answer")
        break 