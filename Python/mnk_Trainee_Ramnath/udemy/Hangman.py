import random
# todo: get random word

word=["apple","orange","banana","mango"]
random_word=random.choice(word)
print(random_word)
# todo: Create blank underscore for random
placeholder=""
for _ in random_word:
    placeholder+="_"
print(placeholder)

game_over=False
output=[]
lives=6

while not game_over:
    # TODO: tell user how many lives left
    print(f"*************{lives} lives left*********")
    # Ask user to guess a letter
    guess_letter=input("Guess a letter : ")

    # TODO: If user entered already gueesed word then print you already gueesed letter

    if guess_letter in output:
        print(f"You have already guessed a letter {guess_letter}")

    # Replacing blanks with guess letter
    display=""

    for letter in random_word:
        if letter==guess_letter:
            display+=letter
            output.append(letter)
        elif letter in output:
            display+=letter
        else:
            display+="_"
    print(display)

    # TODO: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess_letter not in random_word:
        lives-=1
        print(f"You guessed letter {guess_letter},that's not in the word.You lose a life")

        if lives==0:
            print("Game over")
            game_over=True


    if "_" not in display:
        print(f"you win.You guessed correct word {random_word}")
        game_over=True





