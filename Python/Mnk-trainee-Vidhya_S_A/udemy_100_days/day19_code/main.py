#Event listeners : it is a programming construct that when ever an event occurs(.i.e.mouse click , keys)  the corresponding action is trigerred and executed .
from turtle import Turtle,Screen

my_turtle = Turtle()
my_screen = Screen()

def forwards():
    my_turtle.forward(25)

def backwards():
    my_turtle.backward(25)

def turn_left():
    my_turtle.left(10)

def turn_right():
    my_turtle.right(10)

def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()              

my_screen.listen()
my_screen.onkey(forwards,"f")
my_screen.onkey(backwards,"b")
my_screen.onkey(turn_left,"l")
my_screen.onkey(turn_right,"r")
my_screen.onkey(clear_screen,"c")
my_screen.exitonclick()