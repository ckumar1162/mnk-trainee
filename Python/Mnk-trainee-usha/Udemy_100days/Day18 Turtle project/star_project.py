from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.speed("normal")
t.color("red","yellow")
t.begin_fill()
while True:
     t.forward(200)
     t.left(170)
     if t.heading()==0:
         break
t.end_fill()
s.exitonclick()













