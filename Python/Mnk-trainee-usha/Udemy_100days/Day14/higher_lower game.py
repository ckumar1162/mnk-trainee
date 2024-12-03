from operator import truediv

#import game_art
import random
import game_data
#print(game_art.game_logo)
score=0
def display(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description}, from {country}"
def compare(guess,follower1,follower2):
    if follower1>follower2:
        if guess==1:
            return True
        else:
            return False
    else:
        if guess==2:
            return True
        else:
            return False

continue_flag=True
while continue_flag:
    account1 = random.choice(game_data.data)
    account2 = random.choice(game_data.data)
    print(f"compare 1:{display(account1)}")
    #print(game_art.vs)
    print(f"compare 2:{display(account2)}")
    follower1=account1["follower_count"]
    #print(follower1)
    follower2=account2["follower_count"]
    #print(follower2)
    guess=int(input("Enter the Number you want to choose 1 or 2: "))
    is_correct=compare(guess,follower1, follower2)
    if is_correct==True:
        score+=1
        print(f"your are right, your score is {score}")
    else:
        print(f"you are wrong, your score is {score}")
        continue_flag=False
