import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


dictionary = {"+": add, "-": sub, "*": mul, "/": div}

'''continue_loop = True
first_number = float(input("what's the first numbers?:\n"))
while continue_loop:

    operator = input("'+'\n'-'\n'*'\n'/'\n pick an operation")
    second_number = float(input("what's the next numbers?:\n"))
    my_favourite_calculation = dict[operator]
    final_value = my_favourite_calculation(first_number, second_number)
    print(f"{first_number} {operator} {second_number} = {final_value}")
    continue_calci = input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to start a new calculation:")
    first_number = final_value
    if continue_calci == 'n':
        continue_loop = False'''


def calculator():
    print(art.logo)
    first_number = float(input("what's the first numbers?:\n"))
    continue_loop = True
    while continue_loop:
        for key in dictionary:
            print(key)
        operator = input("pick an operation")
        second_number = float(input("what's the next numbers?:\n"))
        final_value = dictionary[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {final_value}")
        continue_calci = input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to start a new calculation:").lower()
        first_number = final_value

        if continue_calci == 'n':
            continue_loop = False
            print("\n" *20)
            calculator()





calculator()
