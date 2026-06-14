expense_name = []
expense_amount = []

while True:
  try:
    print(""" ===Expense Tracker===
1. Add Expense
2. View expenses
3. Show total spending
4. Exit
""")

    option = int(input("Choose an option: "))

    if option == 1:
      name = input("Enter your expense name: ")
      amount = float(input("Enter your expense amount: "))

      expense_name.append(name)
      expense_amount.append(amount)

      print(f"{name} added with amount {amount} successfully")

    elif option == 2:
      if not expense_name:
        print("No expenses recorded.")
      else:
        for name, amount in zip(expense_name, expense_amount):
          print(f"{name}: {amount}")

    elif option == 3:
      total_spending = sum(expense_amount)
      print(f"Total spending: {total_spending}")

    elif option == 4:
      print("Exiting the program. Goodbye!")
      break

    else:
      print("Invalid option. Please choose 1-4.")

  except ValueError:
    print("Invalid input. Please enter a valid option or amount.")
  except KeyboardInterrupt:
    print("Program interrupted. Exiting gracefully.")
    break