'''Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.'''

num = int(input("enter the number: "))
if num % 2 == 0:
    print('even')
else:
    print('odd')
    