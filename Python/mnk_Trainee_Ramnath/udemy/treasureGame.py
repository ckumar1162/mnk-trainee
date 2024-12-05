from queue import PriorityQueue

print("Welcome to treasure Island!")
print("your mission is find the treasure")
s1=input("You want to go right or left? \n").lower()
if s1=="left":
    s2=input('You come to a lake.'
             'There is a an island in the middle of the lake\n'
             'Type "wait" to wait for a boat.'
             'Type "swim" to swim across \n').lower()
    if s2=="wait":
        s3=input("You arrived at island unharmed"
                 "There is a house with 3 door.one Red\n"
                 "One yellow and one blue\n"
                 "which color do you choose?\n").lower()
        if s3=="yellow":
            print("you win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")