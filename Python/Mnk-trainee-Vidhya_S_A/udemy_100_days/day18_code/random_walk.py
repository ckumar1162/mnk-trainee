from turtle import Turtle , Screen
import random 


my_turtle = Turtle()
colour =colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", 
    "brown", "black", "white", "gray", "cyan", "magenta", "lime", 
    "indigo", "violet", "gold", "silver", "beige", "maroon", 
    "navy", "olive", "teal", "coral", "salmon", "khaki", 
    "lavender", "turquoise", "azure", "ivory"
]

directions = [0,90,180,270]
my_turtle.pensize(10)
my_turtle.speed("fastest")

for i in range(100):
    my_turtle.color(random.choice(colour))
    my_turtle.forward(20)
    my_turtle.setheading(random.choice(directions))










my_screen = Screen()
my_screen.exitonclick()

