#password generator
#hard level
import random
number=['1','2','3','4','5','6','7','8','9','0']
letter=['a','b','c','d','e','f','g','h','i','j','k','A','B','G','I','K','U','D']
symbol=['!','@','#','%','*']
print("Welcome to password generator")
nr_number=int(input("How many number you want\n"))
nr_letter=int(input("How many letter you want\n"))
nr_symbol=int(input("How many symbol you want\n"))
password_list=[]
for i in range(0,nr_number):
    password_list.append(random.choice(number))
for i in range(0,nr_letter):
    password_list.append(random.choice(letter))
for i in range(0,nr_symbol):
    password_list.append(random.choice(symbol))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=" "
for i in password_list:
    password+=i
print(password)
