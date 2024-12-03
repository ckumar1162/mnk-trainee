import random
a=random.randint(3,100)
print(a)

b=random.random()
print(b)

c=random.uniform(1,10)
print(c)

d=random.triangular(1,10,2)
print(d)

c=random.randint(0,1)
if c == 0:
    print("Head")
else:
    print("Tail")