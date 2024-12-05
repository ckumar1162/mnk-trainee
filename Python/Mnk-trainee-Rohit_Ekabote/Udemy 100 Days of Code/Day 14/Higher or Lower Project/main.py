import random
import art
import game_data
print(art.logo)


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return  user_guess == 'b'


account_b = random.choice(game_data.data)
score = 0
game_should_continue = True

while game_should_continue:

    account_a = account_b
    account_b = random.choice(game_data.data)
    if account_a == account_b:
        account_b = random.choice(game_data.data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("who has more followers? Type 'A' or 'B' :").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"you are correct, you current score {score}")
    else:
        print(f"sorry you are wrong, final score: {score}")
        game_should_continue = False
