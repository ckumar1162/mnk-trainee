# to create multiple dimension
import random
from turtle import Turtle ,Screen
t=Turtle()
s=Screen()
#TK color specification string
l=["alice blue","beige","cadet blue","dark blue","firebrick","gainsboro","honeydew","indian red","khaki","lavender ","magenta"]
for i in range(3,9):#3,4,5,6,7,8
    angle=360/i
    t.pencolor(random.choice(l))
    for j in range (i):#0,1,2
        t.forward(100)
        t.right(angle)
s.exitonclick()