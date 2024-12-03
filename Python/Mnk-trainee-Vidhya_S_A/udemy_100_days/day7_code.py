#Hangman Project
import random


l1 = ['apple','banana','mango']
lives = 6
guessing_word = random.choice(l1)
#print(guessing_word)

empty = ""
for i in range(len(guessing_word)) :
    empty += "_"
print(empty) 

game_over = False
correct_letter = []
while not game_over:    
    userinput = input("Guess a letter:\n").lower()
    display = ""
    for i in guessing_word:
        if i ==userinput :
             display +=i
             correct_letter.append(i)
        elif i in correct_letter:
            display +=i     
        else:
            display +="_"
    print(display)            

    if userinput not in guessing_word:
        lives -=1
        print("you lose")


    if "_" not in display:
        game_over = True
        print("You won")
       