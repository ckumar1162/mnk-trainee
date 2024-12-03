#tip calculator
print("Welcome to tip calculator!")
total_bill = eval(input("Enter the total bill?\n"))
tip = eval(input("How much tip would u like to pay?10%,12% OR 15%\n"))
split = eval(input("How many people to split the bill?\n"))
each_person = round((total_bill * (tip/100) + total_bill) / split , 2)
print(f"Each person should pay {each_person}")