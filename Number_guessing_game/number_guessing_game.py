
import random

random_number = random.randint(1, 100)
print("Welcome to number guessing game!")

try:
    while True:
        guess = int(input("Guess the number between 1 to 100: "))

        if guess == random_number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
except KeyboardInterrupt:
    print(f"Game cancelled by user. The number was {random_number}.")