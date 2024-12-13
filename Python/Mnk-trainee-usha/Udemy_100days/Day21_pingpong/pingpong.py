from turtle import Turtle,Screen
from ball import Ball
from score import Score
import time
t=Turtle()
t1=Turtle()
s=Screen()
score=Score()


s.bgcolor("black")
s.setup(width=800,height=600)
s.title("PingPong")
s.tracer(0)#to turn off the animation,to make it visible when needed we are using while loop

#create paddle and move it
t.shape("square")
t.shapesize(5,1)
t.color("white")
t.penup()
t.goto(350,0)

#2nd block or paddel
t1.shape("square")
t1.shapesize(5,1)
t1.color("white")
t1.penup()
t1.goto(-350,0)


def up():
    new_y=t.ycor()+20
    t.goto(t.xcor(),new_y)
def down():
    new_y=t.ycor()-20
    t.goto(t.xcor(),new_y)

def lup():
    new_y=t1.ycor()+20
    t1.goto(t1.xcor(),new_y)
def ldown():
    new_y=t1.ycor()-20
    t1.goto(t1.xcor(),new_y)
ball=Ball()


s.listen()
s.onkey(fun=up,key="Up")
s.onkey(fun=down,key="Down")
s.onkey(fun=lup,key="w")
s.onkey(fun=ldown,key="s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    s.update()
    ball.move()

    #Detecing collision with the ball
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()

     #detecting collision with right paddle i.r t1
    if ball.distance(t) <50 and ball.xcor()>320 or ball.distance(t1) <50 and ball.xcor()<-320:
        ball.x_bounce()

    #detect right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    # detect left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

s.exitonclick()