print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_percentage = tip / 100

total_tip_amount = bill * tip_percentage

total_bill = bill + total_tip_amount

split_bill = total_bill / people

final_amount = round(split_bill,2)
print(f"each {people} people should pay: ${final_amount}")