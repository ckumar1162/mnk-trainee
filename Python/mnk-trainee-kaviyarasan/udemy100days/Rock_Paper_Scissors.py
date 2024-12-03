# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
import random

print("welcom to the game rock paper scissor")

user_choice = input("Enter your choice rock paper scissor:").lower()

rps = ["rock", "paper", "scissor"]

ai_bot = random.choice(rps)

print(f"computer choice {ai_bot}")
if user_choice == ai_bot:
    print("Game draw")

elif user_choice == "scissor" and ai_bot == "paper":
    print("you won")
elif user_choice == "paper" and ai_bot == "scissor":
    print("computer won")
elif user_choice == "scissor" and ai_bot == "rock":
    print("you lose")
elif user_choice == "rock" and ai_bot == "scissor":
    print("you won")
elif user_choice == "rock" and ai_bot == "paper":
    print("you lose")
elif user_choice == "paper" and ai_bot == "rock":
    print("you won")
else:
    print("Enter correct value")