import  os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
dict={
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
    }
def calculator():
    num1=int(input("Enter the first number: "))
    for i in dict:# to iterate through the dict to get the symbol
        print(i)
    continue_flag=True
    while continue_flag:
        symbol=input("Enter the operation: ")#+
        num2=int(input("Enter the second number: "))
        #according to + symbol we can fetch add function in dict
        calci=dict[symbol]# this wiil give the value in dict,if it is add ,add is stored in calci ,then we have to pass the number
        output=calci(num1,num2)
        print(f"{num1} {symbol} {num2} = {output}")
        should_continue=input(f"Enter 'y' to continue with {output} or 'n' to start a new calculation or 'x' exit: ").lower()
        if should_continue == "y":
            num1=output # output will be 2nd number while()
        elif should_continue == "n":
            continue_flag=False
            os.system('cls') # to start new calculation in new page
            calculator()# used a recursive function to start new caluclation
        else:
            continue_flag=False
            print("Bye")
calculator()