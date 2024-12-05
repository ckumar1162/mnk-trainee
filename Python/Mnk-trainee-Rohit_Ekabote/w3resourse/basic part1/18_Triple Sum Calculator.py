'''Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.'''

n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
n3 = int(input("enter third number: "))
sum = n1 + n2 + n3
if n1 == n2 == n3:
    print(sum * 3)
else:
    print(sum)
#or

def sum1(x, y, z):
    sum = x+y+z
    if x == y == z:
        sum *= 3
    return sum
print(sum1(n1, n2, n3))