import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters=int(input("enter the number of letters\n"))
n_num=int(input("enter thr number of number\n"))
n_symbols=int(input("enter the number symbols\n"))

password_list=[]
for char in range(0,n_letters):
    password_list.append(random.choice(letters))
for char in range(0,n_num):
    password_list.append(random.choice(numbers))
for s in range(0,n_symbols):
    password_list.append(random.choice(symbols))
print(password_list)

random.shuffle(password_list)
print(password_list)

password=""
for i in password_list:
    password+=i
        
print(f"your password is: {password}")