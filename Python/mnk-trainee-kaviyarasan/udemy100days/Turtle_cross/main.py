import time
from turtle import Screen
from player import Player
from cars import Car

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Cross The Road")
screen.tracer(0)

player = Player()
cars = Car(screen)

screen.listen()
screen.onkey(player.move_front, "Right")
screen.onkey(player.move_back, "Left")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car[0]) < 25:
            game_on = False

    if player.xcor() > 360:
        player.goto(-360, 0)
        cars.level_up()

screen.exitonclick()
