from turtle import Turtle,Screen
t=Turtle()
s=Screen()
print(s.screensize())
t.shape("turtle")
t.penup()
t.goto(300,-250)
t.pendown()
t.dot(20)
t.left(180)
for i in range(11):
        t.forward(40)
        t.dot(20)
t.right(90)
s.exitonclick()

#pending