import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from udemy.Day23.scoreboard import Scoreboard

# from scoreboard import Sc

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p=Player()

c=CarManager()

sco=Scoreboard()


screen.listen()
screen.onkey(p.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    c.create_car()
    c.move_backward()

    # Detect collision with car
    for car in c.all_cars:
        if car.distance(p)<20:
            game_is_on=False
            sco.game_over()

    # detect collision with player
    if p.finish_line():
        p.go_to()
        c.speed_up_car()
        sco.score_update()



screen.exitonclick()