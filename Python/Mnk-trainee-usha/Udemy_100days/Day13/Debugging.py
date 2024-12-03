#describe the problum
# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("you got it")
# my_function()
from typing import Final

#reproduce the bug
# from random import randint
# dice_images=["1","2","3","4","5","6"]
# dice_num=randint(0,5)
# print(dice_images[dice_num])

#play computer
# year=int(input("whats your birth year: "))
# if year>1980 and year<=1994:
#     print("your a millennial")
# elif year>1994:
#     print("Your a GenZ")
# else:
#     print("Nonsense")

#fix thr error
# try:
#     age=int(input("Enter your age"))
# except ValueError:
#     print("enter the number")
#     age=int(input("What is your age"))
# if age >18:
#     print(f"you can drivr at {age}")
# else:
#     print(f"you cant drive at {age}")

#print
# words_per_page=0
# pages=int(input("Number of pages: "))
# words_per_page=int(input("Enter number of words in page: "))
# total_words=pages*words_per_page
# print(total_words)

#debugger
import random
import math
def mutable(a_list):
    b_list=[]
    new_item=0
    for item in a_list:
        new_item=item*2
        new_item+= random.randint(1,3)
        new_item=math.add(new_item,item)
        b_list.append(new_item)
    print(b_list)
mutable([1,2,3,4,5,6,15])