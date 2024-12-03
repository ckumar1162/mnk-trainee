print("Welcome to pizza deliveries")
size=input("What size pizza do you want? S,M,L:")
pepperoni=input("Do you want pepperoni on your pizza? Y or N")
cheese=input("Do you want extra cheese? Y or N")
bill=0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
else:
    bill+=25

if pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if cheese == "Y":
    bill+=1
print(f"The total bill is:{bill}")