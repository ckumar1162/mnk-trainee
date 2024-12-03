print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nchoice correct way or you will be lost in the deep forest ")
choice = input("choice the correct way to find the treasure,"
               "\n type 'left' or 'right':").lower()

if choice == "right":
    print("you choice the correct way move to second stage of the treasure hunt")
    choice2 = input("\nyou have reach the top of the cliff,"
          ",now you need to cross the valley with a dangerous cave sysytem,"
          "\nTwo crossing option are available 'parachute' or 'Zip line' : "
          "").lower()
    if choice2 == 'zip line':
        print("\nYou made a good choice,"
              "congratulations you cross safely through valley")
        choice3 = input("You stand before two ancient doors:"
                        "Behind one of these doors lies the treasure;"
                        " the other leads to an empty room"
                        " \none on the 'right' and one on the 'left'.").lower()
        if choice3 == 'left':
            print("\nYou made it congratulation, Take the treasure and enjoy")
        else:
            print("you lose better luck next time ")

    else:
        print("Made a wrong choice the wind blow you off, "
              "Better luck next time.")
else:
    print("you lost better luck next time")