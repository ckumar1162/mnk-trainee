import random
letters=['a','b','c','d','e','f']
numbers=['0','1','2','3','4','5']
symbols=['!','#','$','%']

print("welcome to pypassword Generator!")
ltr=int(input("how many letters u like to add:\n"))
no=int(input("how many no u like to add\n"))
spl=int(input("how many spl u like to add\n"))
l1=random.sample(letters,ltr)
l2=random.sample(numbers,no)
l3=random.sample(symbols,spl)

l=[]

l.extend(l1)
l.extend(l2)
l.extend(l3)
random.shuffle(l)

l4=" ".join(l)
print(l4)