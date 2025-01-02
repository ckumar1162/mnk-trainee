def add(*args):
    print(type(args))
    print(args[1])
    sum = 0
    for i in args:
        sum +=i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7))


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car =Car(make="nissan", model="skyline")
print(my_car.model)