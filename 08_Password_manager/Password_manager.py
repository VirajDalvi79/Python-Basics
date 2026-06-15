passwords = {}
master_code = "codewithshadow"
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
      3. delete a password   
      4. Exit""")
   option = int(input("Choose an option: "))
   

   if option == 1:
    where = input("Which password is this (e.g., 'email', 'bank', etc.): ")      
    code = input("Enter a password to store: ")
    passwords[where] = code
    with open("passwords.txt", "w") as file:
       print("Password saved successfully.")
       for where, code in passwords.items():
          file.write(f"{where} : {code}\n")
    
    
   elif option == 2:
    view = str(input("which password do you want to view?: "))
    master = input("Enter the master code to view the password: ")
    if master == master_code:
       pass
    else:
         print("Incorrect master code. Cannot view the password.")
         continue
    
    if view in passwords:
      print(f"The password for {view} is : {passwords[view]}")
    else:
        print("Password not found.")

   elif option == 3:
        delete_website = input("Which password do you want to delete?: e.g., 'email', 'bank', etc.: ")
        master = input("Enter the master code to delete the password: ")
        if master == master_code:
           pass 
        else:
             print("Incorrect master code. Cannot delete the password.")
             continue

        if delete_website in passwords:
           del passwords[delete_website]
           print(f"Password for {delete_website} deleted successfully.")
           with open("passwords.txt", "w") as file:
              for where, code in passwords.items():
                 print(file.name)
                 file.write(f"{where} : {code}\n")
                 

   elif option == 4:              
        print("Exiting the program. Goodbye!")
        break
   
 
 except ValueError:
     print("Invalid input. Please enter a valid option.")

 except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting gracefully.")
    break   