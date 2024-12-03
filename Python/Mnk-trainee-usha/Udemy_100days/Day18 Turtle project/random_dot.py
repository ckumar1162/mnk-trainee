import random
import turtle
from turtle import Turtle,Screen
t=Turtle()
s=Screen()
turtle.colormode(255)
print(s.screensize())
t.speed("fastest")
for i in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor((r, g, b))
    t.dot(20)
    t.penup()
    t.goto(random.randint(-300,300),random.randint(-300,300))
    t.pendown()
s.exitonclick()