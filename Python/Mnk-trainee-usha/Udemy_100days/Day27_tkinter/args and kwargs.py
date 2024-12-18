#args:many positional arguments
def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)

add(1,2,3,4,5,6,7,9,10)


#kwargs:many keyword argument
def calculate(n,**kwargs):
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=5)