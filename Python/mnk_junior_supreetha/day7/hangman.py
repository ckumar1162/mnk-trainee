import random

# List of words to choose from
word_list = ['aardvark', 'baboon', 'camel']
choice = random.choice(word_list)
print("Pssst, the word is:", choice)  # Cheat code for testing

# Placeholder for the word with blanks
display = "_" * len(choice)
print(display)

# Game variables
game_over = False
lives = 6
correct_letters = []

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")

    # Update display for correct guesses
    new_display = ""
    for i in range(len(choice)):
        if choice[i] == guess:
            new_display += guess
        else:
            new_display += display[i]
    display = new_display

    # Check if the guess is wrong
    if guess not in choice:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print("You lose! The word was:", choice)
    else:
        print("Correct guess!")
          # Display current progress
    print(display)

    # Check if the player has won
    if "_" not in display:
        game_over = True
        print("You win!")

# End of the game
print("Game over.")
