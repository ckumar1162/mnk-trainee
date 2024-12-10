import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number_to_guess = random.randint(1, 100)

attempts = 0

while True:
    guess = input("Please enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(guess)
    
    attempts += 1
    
    if guess < number_to_guess:
        print("Your guess is too low. Try again!")
    elif guess > number_to_guess:
        print("Your guess is too high. Try again!")
    else:
        print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
        break