def add(*args):
    n=0
    for i in args:
        n+=i
    return n

result=add(3,2,1,7)
print(result)

def add(**kwargs):
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['b'])
add(a=10,b=5)