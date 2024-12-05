def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "did not provided input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("what is your first name? :\n"), input("what is your last name? : \n")))

def canBuyAlcohol(age):
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
print(canBuyAlcohol(int(input("enter your age"))))