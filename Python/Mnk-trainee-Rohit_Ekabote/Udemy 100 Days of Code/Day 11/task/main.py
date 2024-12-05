import art
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0 :
        return "lose, opponent has blackjack"
    elif u_score == 0:
        return "win with a blackjack"
    elif u_score > 21:
        return " you went over, you lose"
    elif c_score > 21:
        return "opponent went over, you won"
    elif u_score > c_score:
        return "you won!"
    else:
        return "you lose"


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f" computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("do you want to play a game of blackjack?  Type 'y' or 'n':\n").lower() == 'y':
    play_game()

'''start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
if start == 'y':
    print(art.logo)
    user = []
    computer = []
    for i in range(2):
        user.append(cards[random.randint(0, 12)])
        computer.append(cards[random.randint(0,12)])
    user_score = 0
    for i in user:
        user_score +=i
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")
    print("Type 'y' to get another card, type 'n' to pass:")'''