from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(tim)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"you've won! the {winning_colour} turtle is the winner!")
            else:
                print(f"you've lost! the {winning_colour} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
