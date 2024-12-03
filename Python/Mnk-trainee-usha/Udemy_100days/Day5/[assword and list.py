#finding the highest number in the list
from password_generator import nr_symbol

# student_score= [199,234,90,67,250,65,89,45,98,100]
# max_score=0
# for score in student_score:
#     if score >max_score:
#         max_score=score
# print(max_score)
#
# #to add number from 1 to 100
# total=0
# for num in range(1,101):
#     total+=num
# print(total)

import random
number=['1','2','3','4','5','6']
letter=['a','b','c','d','e','f','g','h','i','j','k','m','A','B','C','D','E','F','G']
symbol=['@','!','#','$','%','&','*']

print("Welcome to password generator")
nr_number=int(input("How many numbers you want\n"))
nr_letter=int(input("How many letter you want\n"))
nr_symbol=int(input("How many symbol you want\n"))
password=" "

for i in range(1,nr_number + 1):
    password+=random.choice(number)
for i in range(1,nr_letter + 1):
    password+=random.choice(letter)
for i in range(1,nr_symbol + 1):
    password+=random.choice(symbol)

print(f"your password is:{password}")