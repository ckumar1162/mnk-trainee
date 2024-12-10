
from turtle import Turtle,Screen


my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
#draw a square using turtle library
# for i in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

#draw a dashed line 
# for i in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()


#draw different shapes
def shapes(sides):
    angle = 360/sides
    for i in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for shapes_side in range(3,11):
    shapes(shapes_side)    
    

my_screen = Screen()
my_screen.exitonclick()


