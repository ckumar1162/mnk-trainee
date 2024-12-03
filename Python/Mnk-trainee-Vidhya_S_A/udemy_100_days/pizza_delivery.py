
print("Welcome to Vithi's Pizza ^-^")
size = input("What size pizza do u want? S,M or L:")
pepperoni = input("Do u want pepperoni on ur pizza? Y or N:")
extra_cheese = input("Do u extra cheesee? Y or N:")

if size == 'S':
    bill = 50
    if pepperoni == "Y":
        bill += 20
    if extra_cheese == "Y":
        bill +=10
elif size == "M":
    bill = 100
    if pepperoni == "Y":
        bill += 30
    if extra_cheese == "Y":
        bill +=10
elif size == "L":
    bill = 150
    if pepperoni == "Y":
        bill += 30
    elif extra_cheese == "Y":
        bill +=10
else:
    print("Please select any of the option")

print(f"your total bill is {bill}")            