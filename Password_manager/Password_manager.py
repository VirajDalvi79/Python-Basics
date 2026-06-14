passwords = {}
try:
   with open("passwords.txt", "r") as file:
    for line in file:
      where, code = line.strip().split(" : ")
      passwords[where] = code
except FileNotFoundError:
   print("No existing password file found. Starting with an empty password manager.")
   pass

while True:
 try:
   print("""=== Password Manager ===
      1. Store a password
      2. View stored passwords
      3. Exit""")
   option = int(input("Choose an option: "))
   

   if option == 1:
    where = input("Which password is this (e.g., 'email', 'bank', etc.): ")      
    code = input("Enter a password to store: ")
    passwords[where] = code
    with open("passwords.txt", "w") as file:
       print(file.name)
       for where, code in passwords.items():
          file.write(f"{where} : {code}\n")
    
    
   elif option == 2:
    view = str(input("which password do you want to view?: "))
    if view in passwords:
      print(passwords[view])
    else:
        print("Password not found.")

   elif option == 3:
        print("Exiting the program. Goodbye!")
        break
   
 
 except ValueError:
     print("Invalid input. Please enter a valid option.")

 except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting gracefully.")
    break   