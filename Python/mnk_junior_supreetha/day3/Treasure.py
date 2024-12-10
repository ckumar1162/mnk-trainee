print("Welcome to Treasure Island Your mission is to find the treasure")
direction=input("You are in crossroad ,which direction you want to go ? Type 'left' or 'right'\n ")
if direction == "left" or "Left":
    
    choice2=input("you have reached the lake,Do you want to 'wait' for the boat or 'swim'\n")
    if choice2 == "wait":
        
        choice3 = input("You have arrived at island. "
                        "There are 3 doors in house one red, one yellow,one blue. "
                        "which one you want to choose.\n ")
        if choice3 == "red" or "Red":
            print("Its room full of fire.Game over")
        elif choice3 == "Yellow" or "yellow":
            print("You found the treasure.You won")
        elif choice3 == "blue" or "Blue":
            print("You have entered room full of ghost.Game over")
        else:
            print("You have entered a wrong option")
    else:
        print("There were lots of crocodile in the lake ,Game over")

else:
    print(" You fell into hole,Game over")