import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

#creating objects for the above class
player1 = Player()
car = CarManager()
score = Scoreboard()


#adding event listeners to get input from keys
screen.listen()
screen.onkey(player1.move_up,"v")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    #detect collision with the car
    for car1 in car.all_car:
        if car1.distance(player1) < 20:
            game_is_on = False
            score.game_over()

    # check player crossed
    if player1.crossed():
        player1.go_to_start()
        car.car_speed()
        score.level_up()

screen.exitonclick()