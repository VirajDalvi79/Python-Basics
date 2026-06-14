expense_name = []
expense_amount = []



while True:

 print(""" ===Expense Tracker===
      1. Add Expense
      2. view expense
      3. show total spending 
      4. exit
      """)

 option = int(input("choose an option: "))

 if option == 1:
   
   name = input("Enter your expense name: ")
   amount = float(input("Enter your expense amount: "))

   expense_name.append(name)
   expense_amount.append(amount)

   print(f"{name} added with amount {amount} successfully")

 elif option == 2:
   
     for name, amounts in zip(expense_name, expense_amount):
       print(f"{name}: {amounts}")

 elif option == 3:
       total_spending = sum(expense_amount)
      
       print(f"Total spending: {total_spending}")      
 
 elif option == 4:
         print("Exiting the program. Goodbye!")
         break