# function is to compare values from dictionary and print results
def com_bid(dic):
    high_aoumnt = 0
    name = ""
    for i in dic:
        bid=dic[i]
        if bid>high_aoumnt:
            high_aoumnt=bid
            name=i

    # high_aoumnt = max(dic, key=dic.get)
    print(f"The winner is {name} with bid of: $ {high_aoumnt}")

dic={}
condition=True
while condition:
    name=input("Enter the name:\n")
    bid_amount=int(input("Enter the bid amount: $ \n"))

    dic[name]=bid_amount
    print(dic)

    choice = input("Is there anyone to bid? yes or no:\n")
    if choice=="no":
        condition=False
        # call function to compare values and print results
        com_bid(dic)
    # clear screen so other person shouln't know bid amount
    elif choice=="yes":
        print("\n" *20)



