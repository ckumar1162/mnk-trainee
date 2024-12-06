print("Welcome to the tip calculator!")
a=float(input("What was the total bill? $"))
b=int(input("How much tip would you like to give? 10,12 or 15?"))
c=int(input("How many people to split the bill?"))
bill_with_tip=a+b
print(bill_with_tip)
final=print(f"Each person should pay {bill_with_tip/c}")