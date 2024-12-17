from turtle import Turtle,Screen
import time


s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake Game")
turtle_position=[(0,0),(-20,0),(-40,0)]
segments=[]
s.tracer(0)
# TODO : Creating a 3 turtles with its position

is_game_on=True
while is_game_on:
    s.update()
    time.sleep(0.1)

    for seg in range(len(segments)-1, 0, -1):
        new_x=segments[seg-1].xcor()
        new_y=segments[seg-1].ycor()
        segments[seg].goto(new_x,new_y)
    segments[0].forward(20)











s.exitonclick()