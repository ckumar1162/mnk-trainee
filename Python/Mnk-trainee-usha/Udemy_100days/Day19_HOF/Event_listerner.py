import turtle
from turtle import Turtle,Screen
t=Turtle()
s=Screen()

def up():
    t.setheading(90)
    t.forward(20)
def down():
    t.setheading(270)
    t.forward(20)
def left():
    t.setheading(180)
    t.forward(20)
def right():
    t.setheading(0)
    t.forward(20)
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


turtle.listen()
s.onkey(fun=up,key="Up")
s.onkey(fun=down,key="Down")
s.onkey(fun=left,key="Left")
s.onkey(fun=right,key="Right")
s.onkey(fun=clear_screen,key="c")

s.exitonclick()