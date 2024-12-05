print("welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10 ,12 or 15? "))
split=int(input("How many people to split the bill? "))
# total_tip=tip/100*bill+bill
tip_as_percent=tip/100
tip_amount=tip_as_percent*bill
total_amount=tip_amount+bill
total_bill=total_amount/split
final_bill=round(total_bill,2)
print(f"Each person should pay ${final_bill}")

