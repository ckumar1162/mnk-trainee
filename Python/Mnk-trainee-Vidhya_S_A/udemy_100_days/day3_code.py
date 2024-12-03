#Treasure Island
print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to Treasure Island!\n Your mission is to find the treasure.\n ")
direction = input("You are at a cross road . Where do you want to go\n          Type Left or right.\n").upper()
if direction == "LEFT":
    boat = input("You've come to lake.There is an Island in the middle of the lake \n Type WAIT to wait for a boat or type SWIM to swim across.\n").upper()
    if boat == "WAIT":
        print("Yahoo^-^ !!! You arrived at the Island.\n")
        room = input("There was Three doors. one Green,yellow and red.Which one would u choose \n ").upper()
        if room == "GREEN":
             print("Yahoooo!!!!!!!\n   Congratualations . You won (^_^)")
        else:
            print("Game over (-_-)")
    else:
       print("Oh no , there was an alligator . Game over")
else:
    print("Oops! You caught by a monster.Game over")

