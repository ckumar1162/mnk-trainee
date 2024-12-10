print("Welcome to roller coster")
height=int(input("Enter your height?"))
bill=0
if height > 120:
     print("you can ride the roller coaster")
     age=int(input("Enter your age"))
     if age <= 12:
         print("Please pay $5")
         bill=5
     elif age <= 18:
         print("Please pay $7")
         bill=7
     else:
         print("Please pay $12")
         bill=12
     photo=input("Do you want photo,if yes press Y,If no press N")
     if photo == "Y":
         pbill=bill+3
         print(f"your total bill is:{pbill}")
     else:
         print(f"your total bill is:{bill}")


else:
    print("you can't ride the roller coaster")
