# import the models needed
from game_data import data
from random import choice
from art import logo

# getting the user input to start the game
user_start = input("Enter start to begin :").lower()
while not user_start == "start":  # if user enter wrong it will loop again and get user input
    user_start = input("Enter start to begin :").lower()



# creating a function to call the game
def game():
    continue_game = True
    user_score = 0 # to count the score

    bot_choice1 = choice(data) # choice a random data
    bot_choice2 = choice(data)

    while bot_choice1 == bot_choice2: # if the choice1 and choice2 or same choice again the choice 2
        bot_choice2 = choice(data)


    while continue_game:
        # printing the choice1 data
        print("\nname:", bot_choice1["name"], "\nfollower_count:", bot_choice1["follower_count"], "million",
              "\ndescription:", bot_choice1["description"], "\ncountry:", bot_choice1["country"])

        print(logo) # printing a logo higher or lower

        # printing the choice2 data
        print("\nname:", bot_choice2["name"], "\nfollower_count: ?", "\ndescription:", bot_choice2["description"],
              "\ncountry:", bot_choice2["country"])
        # print(f"Current score : {user_score}")
        # getting input from the user to guess higher or lower
        guess = input("guess the inst_user would have higher follower or lower: ")

        # checking the user guess is correct or wrong
        if guess == "higher":
            is_correct = bot_choice1["follower_count"] < bot_choice2["follower_count"]
        elif guess == "lower":
            is_correct = bot_choice1["follower_count"] > bot_choice2["follower_count"]
        else:
            print("Invalid input. Please type 'higher' or 'lower' :")
            continue # continue till user enter a correct value

        if is_correct:
            user_score +=1 # increment the score
            print(f"your right, current score : {user_score}")
            bot_choice1 = bot_choice2
            bot_choice2 = choice(data)

            while bot_choice1 == bot_choice2:
                bot_choice2 = choice(data)

        else:
            print(f"You loss the game . Final score:{user_score}")
            continue_game = False # end the loop if user guess wrong
game()
