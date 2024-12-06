from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
for _ in range(15):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()

#or

for _ in range(10):
    my_turtle.forward(5)
    my_turtle.color("white")
    my_turtle.forward(5)
    my_turtle.color("black")

screen = Screen()
screen.exitonclick()