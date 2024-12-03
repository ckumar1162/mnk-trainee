import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game = [rock,paper,scissor]
print("ROCK , PAPER , SCISSOR ")
rock_paper_scissor = int(input("Type 0 for rock, 1 for paper , 2 for scissors\n"))
print(game[rock_paper_scissor])       
play = random.randint(0,2)
print("Computer choose:\n")
print(game[play])
if rock_paper_scissor == play:
    print("Draw the match")
elif rock_paper_scissor == 0 and play == 1:
    print("You lose")
elif  rock_paper_scissor == 0 and play == 2:
    print("You win")
elif rock_paper_scissor == 2 and play ==1:
    print("you win")
elif rock_paper_scissor == 1 and play ==0:
    print("you win") 
elif rock_paper_scissor == 1 and play ==2:
    print("you lose")
elif rock_paper_scissor == 2 and play ==0:
    print("you lose")            
else:
    print("Choose proper number")         


    
    
