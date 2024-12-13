from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Your bet", prompt="Which participant will win? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_participants = []

for participant_number in range(6):
    new_participant = Turtle(shape="turtle")
    new_participant.penup()
    new_participant.color(colors[participant_number])
    new_participant.goto(x=-230, y=y_positions[participant_number])
    all_participants.append(new_participant)

if user_bet:
    is_race_on = True

def check_winner(participant, user_bet):
    if participant.xcor() > 230:
        winning_color = participant.pencolor()
        if winning_color == user_bet:
            print(f"You won The {winning_color} participant is the winner")
        else:
            print(f"You lost The {winning_color} participant is the winner")
        return True
    return False

while is_race_on:
    for participant in all_participants:
        if check_winner(participant, user_bet):
            is_race_on = False
            break

        rand_distance = random.randint(0, 10)
        participant.forward(rand_distance)

screen.exitonclick()
