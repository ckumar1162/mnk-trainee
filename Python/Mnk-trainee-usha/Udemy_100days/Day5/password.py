import random
number=['0','1','2','3','4','5','6','7','8','9']
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol=['!','@','#','$','%','&','*','(',')']
print("Welcome to password generator")
nr_number=int(input("How many numbers yo want\n"))
nr_letter=int(input("How many letter you want\n"))
nr_symbol=int(input("How many symbol you want\n"))
#easy level
password =" "
for i in range(1,nr_number + 1):
    password+=random.choice(number)
for i in range(1,nr_letter + 1):
    password+=random.choice(letter)
for i in range(1,nr_symbol + 1):
    password+=random.choice(symbol)
print(password)
#easy level