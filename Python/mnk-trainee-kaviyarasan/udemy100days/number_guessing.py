from random import randrange

guess_num = randrange(1, 100)
user_choice = input("choice the level 'Hard' or 'Easy' : ").lower()

def guess_hard_num():

    life_hard = 5
    print("guess the number 1 to 100")
    print("hard level you got 5 life")
    while life_hard:
        life_hard -= 1
        # print(f"hard level you have {life_hard} life")
        user_guess = int(input("guess the number : "))
        if user_guess > guess_num:
            print(f"life left {life_hard}")
            print("Too High")
        elif user_guess < guess_num:
            print(f"life left {life_hard}")
            print("Too Low")
        else:
            print(f"the number you guess {guess_num}")
            print("You got it!")
    print("life lift 0 you lost")
def guess_easy_num():
    life_easy = 10
    print("guess the number 1 to 100")
    print("you choice the easy level got 10 life ")
    while life_easy:
        life_easy -= 1
        user_guess = int(input("Guess the number: "))

        if user_guess > guess_num:
            print(f"life left {life_easy}")
            print("Too high ")
        elif user_guess < guess_num:
            print(f"life left {life_easy}")
            print("to low")
        else:
            print(f"you got it!{guess_num}")
    print("life left 0 you lost")


if user_choice == "easy":
    guess_easy_num()

elif user_choice == "hard":
    guess_hard_num()

else:
    print(f"invalid choice")



