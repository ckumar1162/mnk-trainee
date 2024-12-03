from turtle import Turtle,Screen
import turtle
import random
t=Turtle()
turtle.colormode(255)
s=Screen()
t.speed("fastest")
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.pencolor((r,g,b))
    t.circle(100)
    t.left(3)
    if t.heading()==0:
        break
s.exitonclick()