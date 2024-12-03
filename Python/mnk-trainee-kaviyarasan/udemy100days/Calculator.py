
def add(n1, n2):
    return n1 + n2
# print(add(6,8))

def sub(n1,n2):
    return n1 - n2
# print(sub(4,2))

def mul(n1,n2):
    return n1 * n2
# print(mul(3, 9))

def div(n1,n2):
    return n1 / n2
# print(div(8, 5))

todo = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculator():
    should_accumulate = True
    num1 = int(input("Enter the first number :"))

    while should_accumulate:

        operations_symbol = input("Enter the operator +, -, *, / :")
        num2 = int(input("Enter the second number :"))
        ans = todo[operations_symbol](num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {ans}")

        choice = input(f"type 'yes' if you want to calculate with answer {ans},if not type no :").lower()

        if choice == "yes":
            num1 = ans
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()

