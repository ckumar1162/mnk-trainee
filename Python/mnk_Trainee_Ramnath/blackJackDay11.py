import random
from zoneinfo import reset_tzpath


# TODO: Hint 4
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def compare(uu_score, cc_score):
    if uu_score==cc_score:
        return "Draw"
    elif cc_score==0:
        return "Lose. opponent has a blackjack"
    elif uu_score==0:
        return "Your win."
    elif uu_score>21:
        return "You Lose"
    elif uu_score>cc_score:
        return "You win"
    else:
        return "YOu lose"

def calculate_score(cards):
    """Take a list of cards and return score calculated from the cards"""
    # Todo : Hint 7
    if sum(cards)==21 and len(cards)==2:
        return 0
    # todo : hint 8
    if 11 in cards and sum(cards)>21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# TODO :  Hint 5
user_card=[]
computer_card=[]
is_game_over=False
c_score=-1
u_score=-1

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

# TODO: Hint 11
while not is_game_over:
    u_score=calculate_score(user_card)
    c_score=calculate_score(computer_card)
    print(f"Your card is : {user_card} and current score is {u_score}")
    print(f"Computer first card {computer_card[0]}")
    # TODO: Hint 9
    if u_score==0 or c_score==0 or u_score>21:
        is_game_over=True
    else:
        # TODO: Hint 10
        is_should_deal=input("Type 'y' to get another card ,type 'n' to no")
        if is_should_deal=='y':
            user_card.append(deal_card())
        else:
            is_game_over=True

while c_score!=0 and c_score<17:
    computer_card.append(deal_card())
    c_score=calculate_score(computer_card)

print(f"Your final hand card {user_card},final score {u_score}")
print(f"Computer final card {computer_card},computer score {c_score}")
compare(u_score,c_score)

