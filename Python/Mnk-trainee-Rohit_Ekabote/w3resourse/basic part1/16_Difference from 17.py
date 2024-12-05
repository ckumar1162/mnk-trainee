'''Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.'''

num1 = int(input("enter the number: "))
if num1 > 17:
    print(abs((num1-17)*2))
else:
    print(abs(17-num1))

#or

def difference():
    num1 = int(input("enter the number: "))
    if num1 > 17:
        return abs((num1-17)*2)
    else:
        return abs(17-num1)
print(difference())