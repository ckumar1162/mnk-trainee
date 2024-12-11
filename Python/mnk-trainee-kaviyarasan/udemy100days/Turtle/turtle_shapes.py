import random
from turtle import Turtle, done
import turtle

turtle.colormode(255)
tim = Turtle()
def sides(num):
    angle = 360 / num
    for i in range(num):
        # r = random.choice()
        tim.color(random_color())
        tim.forward(100)
        tim.right(angle)
def circle(num):
    tim.circle(100)
    tim.setheading(360)
    tim.forward(100)
def random_color  ():
    r = random.randint(0,255)
    g = random.randint(0,255)
    y = random.randint(0,255)
    color = (r, g , y)
    return color
for shape_sides in range(3,11):
    # circle(shape_sides)
    sides(shape_sides)


screen = turtle.Screen()
screen.exitonclick()
