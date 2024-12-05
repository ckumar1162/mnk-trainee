import random

rock="ROCK"
paper="PAPER"
scissor="SCISSOR"

user_choice=int(input("enter the your choice 0 for Rock ,1 for Paper and 2 for scissor?"))
print(f"user choice is:{user_choice}")

computer_choice = random.randint(0, 2)
print(f"computer choice is :{computer_choice}")

if user_choice>=3:
    print("enter valid option")

elif user_choice==computer_choice:
    print("its tie")
elif user_choice==0:
    if computer_choice==1:
        print("you win")
    else:
        print("you lose")
elif user_choice==1:
    if computer_choice==2:
        print("you win")
    else:
        print("you lose")
elif user_choice==2:
    if computer_choice==0:
        print("you win")
    else:
        print("you lose")
