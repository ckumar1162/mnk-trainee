import turtle
from turtle import Turtle,Screen
t=Turtle()
s=Screen()
def left():
    new_heading=t.heading()+20
    t.setheading(new_heading)
    t.forward(20)
def right():
    new_head=t.heading()-20
    t.setheading(new_head)
    t.forward(20)
def move_forward():
    t.forward(20)
def move_backward():
    t.backward(20)
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

turtle.listen()
s.onkey(fun=left,key="l")
s.onkey(fun=right,key="r")
s.onkey(fun=move_forward,key="f")
s.onkey(fun=move_backward,key="b")
s.onkey(fun=clear_screen,key="c")
s.exitonclick()