import random 

length = int(input("Enter the desired length of the password: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?/"
password = ""
while True:
 try:
  for i in range(length):
    password = password + random.choice(characters)
  print("Your generated password is: " + password)
  break

 except ValueError:
  print("Invalid input. Please enter a valid number.")
 except KeyboardInterrupt:
  print("\nGeneration interrupted by user.")
  break