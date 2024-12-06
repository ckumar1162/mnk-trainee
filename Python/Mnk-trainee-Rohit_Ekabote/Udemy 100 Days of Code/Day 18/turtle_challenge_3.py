from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

colors = ["gray", 'dark green', 'yellow green', 'brown',]


def draw(sides):
    angle = 360/sides
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)


for _ in range(3, 8):
    my_turtle.color(random.choice(colors))
    draw(_)


screen = Screen()
screen.exitonclick()
