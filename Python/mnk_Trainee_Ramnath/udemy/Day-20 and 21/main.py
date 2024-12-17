import time
from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard

s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake=Snake()

food=Food()

sco=ScoreBoard()

s.listen()
s.onkey(snake.move_up,"Up")
s.onkey(snake.move_down,"Down")
s.onkey(snake.move_left,"Left")
s.onkey(snake.move_right,"Right")



is_game_on=True

while is_game_on:
    s.update()
    time.sleep(0.1)

    # Collision with Food
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        sco.increase_score()

    # Collision with wall
    if snake.head.xcor() >280 or  snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        is_game_on=False
        sco.game_over()

    #  collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) <10:
            is_game_on=False
            sco.game_over()

    snake.move()



s.exitonclick()