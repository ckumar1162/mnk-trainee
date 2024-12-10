from turtle import Turtle,Screen

tim=Turtle()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def clear():
    tim.home()
    tim.clear()
def move_left():
    tim.left(10)
def move_right() :
    tim.right(10)


screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="c",fun=clear)
screen.onkey(key="l",fun=move_left)
screen.onkey(key="r",fun=move_right)
screen.exitonclick()

