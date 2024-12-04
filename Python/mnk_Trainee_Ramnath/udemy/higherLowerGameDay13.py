import random

import Day13_Data as d

def name_format(accounts):
    name=accounts["name"]
    des=accounts["Description"]
    country=accounts["Country"]

    return f"{name} a {des} from {country}"

# check if user is correct
def check_answer(a_followers,b_followers,gues):
    if a_followers>b_followers:
        return gues=="a"
    else:
        return gues=="b"


score=0

account_b=random.choice(d.data)

Should_continue=True
while Should_continue:
    # generate random account from the game data
    # making account at position B  become the next account at position A
    account_a=account_b
    account_b=random.choice(d.data)
    if account_b==account_a:
        account_b=random.choice(d.data)


    # format account data into printable format
    print(f"Compare A: {name_format(account_a)}")
    print(f"Against B: {name_format(account_b)}")

    # ask user for guess
    guess=input("Enter your option 'A' or 'B': ").lower()

    # Clear screen
    print("\n")


    # get follower count of each account
    count_a =account_a["follow count"]
    count_b = account_b["follow count"]
    #use if statement to check if user is correct
    check=check_answer(count_a,count_b,guess)
    if check:
        score+=1
        print(f"You are right,your current score is {score}")
        Should_continue=True
    else:
        Should_continue=False
        print(f"Sorry.That's wrong Your final score is {score}")




