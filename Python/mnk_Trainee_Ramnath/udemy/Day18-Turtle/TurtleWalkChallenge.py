import random
import turtle as t


tim=t.Turtle()


# color=["cyan","spring green","firebrick","lime","orchid","medium violet red"]
directions=[0,90,180,270]
t.colormode(255)

tim.pensize(15)
tim.speed("fastest")

def set_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    tuple_color=(r,g,b)
    return tuple_color

for _ in range(200):
    tim.color(set_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

