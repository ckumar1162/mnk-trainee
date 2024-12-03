# from turtle import Turtle,Screen
# import random
# t=Turtle()
# s=Screen()
# l=["black","cadet blue","dark blue","firebrick","gainsboro","indian red","khaki","magenta","RosyBrown1","RosyBrown2","RoyalBlue1","sandy brown","SpringGreen4","violet red","yellow"]
# t.pensize(10)
# for _ in range(50):# 50 is how many moves you want
#     t.setheading(random.randrange(0,360,90))
#     t.pencolor(random.choice(l))
#     t.forward(20)
# s.exitonclick()
import turtle
# how to chhose random rgb colors
from turtle import Turtle,Screen
import random
t=Turtle()
s=Screen()
turtle.colormode(255)
t.pensize(10)
for _ in range(50):# 50 is how many moves you want
    t.setheading(random.randrange(0,360,90))
    r=random.randint(0,255)
    g =random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor((r,g,b))
    t.forward(20)
s.exitonclick()