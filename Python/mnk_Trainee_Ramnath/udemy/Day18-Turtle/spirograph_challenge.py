import turtle
import random

t=turtle.Turtle()
turtle.colormode(255)

t.speed("fastest")
def set_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color
def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(set_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
spirograph(5)


s=turtle.Screen()
s.exitonclick()