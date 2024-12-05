from turtle import Turtle,Screen
'''Constructing objects and accessing attributes and methods '''
t=Turtle()
print(t)
t.shape("turtle")
t.forward(50)
t.color("Green")


s=Screen()
print(s.title("TurtleDemo"))
print(s.canvheight)
print(s.canvwidth)
s.screensize(200,bg="skyblue")
s.exitonclick()


