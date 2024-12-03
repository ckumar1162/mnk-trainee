import random
word=["camel","dog",'horse','cat']
a=random.choice(word)
print(a)

c=len(a)
place=""
for i in range(c):
    place+="_"
print(place)
#use while loop to let the user guess again and again

b=input("Guess the letter:\n").lower()
display=""
for i in a:
    if i==b:
         display+=i
    else:
        display+="_"
print(display)