print("Welcome to Pizza Corner!")
size=input("enter the pizza size: S or M or L?")
pepper=input("DO you want to add pepper to pizza? y for Yes and n for No")
ex_cheese=input("do you want extra cheeese: y for Yes and n for NO")
bill=0

if size=="S":
    bill+=15
    if pepper=="y":
         bill+=2


elif size=="M":
    bill+=20
    if pepper=="y":
        bill+=3

elif size=="L":
    bill+=25
    if pepper=="y":
        bill+=3

if ex_cheese == "y":
    bill+=1
    print(f"final bill is $ {bill}")
else:
    print(f"final bill is $ {bill}")