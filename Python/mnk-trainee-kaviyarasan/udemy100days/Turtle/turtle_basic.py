from turtle import Turtle, Screen

from prompt_toolkit.shortcuts import clear

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(15)
def turn_right():
    heading = t.heading() + 10
    t.setheading(heading)
def turn_left():
    heading = t.heading() - 10
    t.setheading(heading)
def move_back():
    t.backward(15)
def clear_c():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(move_forward,"f")
screen.onkey(turn_right,"r")
screen.onkey(move_back,"b")
screen.onkey(turn_left,"l")
screen.onkey(clear_c,"c")
screen.exitonclick()

