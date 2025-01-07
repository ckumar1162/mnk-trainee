import pandas as pd
import random

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    to_learn = pd.read_csv("french_words.csv").to_dict(orient="records")

def next_card():
    global current_card
    if not to_learn:
        print("You have learned all the words!")
        return False
    current_card = random.choice(to_learn)
    print(f"\nFrench: {current_card['French']}")
    print("Flipping the card")
    flip_card()
    return True

def flip_card():
    print(f"English: {current_card['English']}")

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)
    print(f"'{current_card['French']}' has been marked as known!")

print("Flashcard Program Started!")
print("Press 'n' for next card, 'k' if you know the word, or 'q' to quit.")

while True:
    user_input = input("\nEnter your choice: ").strip().lower()
    if user_input == 'n':
        if not next_card():
            break
    try:
        if user_input == 'k':
            is_known()
    except ValueError:
        print("while start the game pls enter 'n'")
        user_input = input("\nEnter your choice: ").strip().lower()

    if user_input == 'q':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Please press 'n', 'k', or 'q'.")
