#calculator program

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def div(n1,n2):
    return n1 / n2

def mul(n1,n2):
    return n1 * n2

calci = {"+" : add,
         "-" : sub,
         "*" : mul,
         "/" : div
        }
should_continue =True
while should_continue:
    should_accumate = True
    f_num = eval(input("Enter the first number ?"))
    while should_accumate:
        for i in calci:
            print(i)
        operator = input("Enter the operator?")
        l_num = eval(input("Enter the last number ?"))

        result = calci[operator](f_num,l_num)
        print(f"{f_num} {operator} {l_num} = {result}")    


        user_wish = input(f"Type 'y' to continue calculation with {result} or type 'n' to start a new calculation: ")

        if user_wish == "y":
            f_num = result

        else:
            should_accumate = False    