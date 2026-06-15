try:
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))

    operator = input("Select an operator [+,-,/]: ")

    while True:
        if operator == "+":
            print(f"{number1} + {number2} = {number1 + number2}")
            break
        elif operator == "-":
            print(f"{number1} - {number2} = {number1 - number2}")
            break
        elif operator == "/":
            if number2 != 0:
                print(f"{number1} / {number2} = {number1 / number2}")
            else:

                print("Cannot divide by zero.")
            break
        else:
            operator = input("Invalid operator, please select a valid operator [+,-,/]: ")
except KeyboardInterrupt:
    print("Operation cancelled by user.")

