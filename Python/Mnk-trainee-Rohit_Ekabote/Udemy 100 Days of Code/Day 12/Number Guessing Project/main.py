from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low")
        return turns - 1
    else:
        print(f"you got it, the answer was {actual_answer}")


def set_difficulty():
    level = input("choose a difficulty, type 'easy' or 'hard'").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"pass the correct answer is {answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")

        guess = int(input("make guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you run out of guess, you loss")
            return
        elif guess != answer:
            print("guess again")


game()
