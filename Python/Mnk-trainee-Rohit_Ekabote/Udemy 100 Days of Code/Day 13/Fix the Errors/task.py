try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed in a an invalid number. please try again with a numerical response like a 17")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
