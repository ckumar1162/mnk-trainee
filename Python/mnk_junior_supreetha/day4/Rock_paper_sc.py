import random
user_choice=int(input("what do u choose?  Type 0 for rock,1 for paper or 2 for scissors\n"))
computer_choice=random.randint(0,3)
print(f"Computer_chice:{computer_choice}")
if user_choice>=3 and user_choice<0:
    print("you typed an invalid number. u lose!")
elif user_choice==0 and computer_choice==2:
    print("u win")
elif user_choice> computer_choice:
    print("u win")
elif user_choice==computer_choice:
    print("game draw")
else:
    print("computer win")