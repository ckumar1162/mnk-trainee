#play computer
# year=int(input("whats your birth year: "))
# if year>1980 and year<=1994:
#     print("your a millennial")
# elif year>1994:
#     print("Your a GenZ")
# else:
#     print("Nonsense")

#fix thr error
# try:
#     age=int(input("Enter your age"))
# except ValueError:
#     print("enter the number")
#     age=int(input("What is your age"))
# if age >18:
#     print(f"you can drivr at {age}")
# else:
#     print(f"you cant drive at {age}")



#leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(2000))