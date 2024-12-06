print("welcome to python Pizza Deliveries!")
size=input("what size pizza do u want? S, M or L:")
bill=0
if size=='S':
    bill+=15
    pepperoni=input("do you want pepperoni on pizza? Y or N:")
    if pepperoni=='Y':
        bill+=2
elif size=='M':
    bill+=20
    pepperoni=input("do you want pepperoni on pizza? Y or N:")
    if pepperoni=='Y':
        bill+=3
else:
    bill=25
    pepperoni=input("do you want pepperoni on pizza? Y or N:")
    if pepperoni=='Y':
        bill+=3
cheese=print(input("do u need extra cheese? Y or N:"))
bill+=1
print("your total bill is:",bill)
        