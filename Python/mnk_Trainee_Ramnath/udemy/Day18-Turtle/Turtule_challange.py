# challenge 1:  Draw a square

import turtle
import random


t=turtle.Turtle()
t.shape("turtle")

# TODO challenge: Draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# TODO challenge: Draw a dashed line
# for _ in range(10):
#      t.forward(10)
#      t.penup()
#      t.forward(10)
#      t.pendown()

# TODO challenge: Drawing a different shapes with colors
colors=["green","blue","pink","red","yellow","orange"]

def draw_shape(num_of_sides):
    angle=360/num_of_sides
    for _ in range(num_of_sides):
        t.forward(100)
        t.right(angle)
for i in range(3,8):
    t.color(random.choice(colors))
    draw_shape(i)








s=turtle.Screen()
s.exitonclick()





