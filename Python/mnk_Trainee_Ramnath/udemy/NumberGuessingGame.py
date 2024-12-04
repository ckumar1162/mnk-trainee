import random
def easy(choices,turn):
    n=turn
    for _ in range(n):
        print(f"you have {n} attempts remaining to guess the number")
        guess=int(input("Make a guess: "))
        if guess==num:
             return f"You got it. The answer was {num}"
        elif guess<num:
            print("Too Low.")
        elif guess>num:
            print("Too high.")
        n+=-1
        if n==0:
            return "You run of out guess."
# def hard():
#     n=5
#     for _ in range(5):
#         print(f"you have {n} attempts remaining to guess the number")
#         guess = int(input("Make a guess: "))
#         if guess == num:
#             return f"You got it. The answer was {num}"
#
#         elif guess < num:
#             print("Too Low..")
#         elif guess > num:
#             print("Too high.")
#         n += -1
#         if n == 0:
#             return "You run of out guess."
#         print("Guess Again")


# Choosing random number between 1 and 100
print("Welcome to number guessing game!")
num=random.randint(1,100)
print(num)
print("I am thinking of number between 1 to 100.")
choice=input("Choose the difficulty. 'easy' or 'hard\n").lower()
# if choice=="easy":
#     result=easy()
#     print(result)
# else:
#     res=hard()
#     print(res)
turns=0
if choice=="easy":
    turns+=10
else:
    turns+=5
print(easy(choice,turns))