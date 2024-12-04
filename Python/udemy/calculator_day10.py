def add(n1,n2):
    return n1+n2
def multi(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2

# TODO add 4 functions to dictionary.keys are : '+','-','*' and '/'
dic={
    "+":add,
    "-":sub,
    "*":multi,
    "/":div
}
def calculator():
    f_num=float(input("Enter the first number "))
    cond=True
    while cond:

        op=input("Enter the operation: +,-,* or /? ")
        s_num=float(input("Enter the second number: "))
        # TODO: If operation in dic then pass 2 values and call function and print output
        if op in dic:
            result=dic[op](f_num,s_num)
            print(f"{f_num} {op} {s_num} ={result}")
        choice=input("You want to continue: yes or no ?").lower()
        if choice=="no":
            cond=False
            calculator()

        elif choice=='yes':
            cond=True
            f_num=result

calculator()
