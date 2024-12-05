#Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("enter the number"))
if abs(1000 - num) <= 100 or abs(2000 - num) <= 100:
    print(True)
else:
    print(False)
    
#or
def function(num):
    if abs(1000 - num) <= 100 or abs(2000 - num) <= 100:
        return True
    else:
        return False
print(function(int(input("enter the number"))))