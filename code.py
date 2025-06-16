import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("🎯 Welcome to the Number Guessing Game!")
print("I've chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

# Loop for max attempts
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempt(s).")
            break
    except ValueError:
        print("Please enter a valid number.\n")

# If user fails to guess
if guess != secret_number:
    print(f"😢 Sorry! You've used all your attempts. The number was {secret_number}.")
