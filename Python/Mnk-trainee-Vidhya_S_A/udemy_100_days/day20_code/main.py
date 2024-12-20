#snake game using turtle and oops concept
from turtle import Screen
from snake_game import SnakeGame
from food import Food
from score import Score
import time


my_screen = Screen()
my_screen.bgcolor("olive")
my_screen.setup(600,600)
my_screen.title("Snake game")
my_screen.tracer(0) #tracer() is used to control the speed of the drawing or toggle the animation  of the turtle movement



snake = SnakeGame()
food = Food()
score = Score()
# adding event listeners to get the direction from the keyboard by the user
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

#move the snake
is_game = True 

while is_game:
    my_screen.update()
    time.sleep(0.2)
    snake.move_snake()   

    #detect collision with the food
    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    #detect collision with the wall
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 299 or snake.segments[0].ycor() < -299:
        score.highscore()
        snake.reset()

    #detection with tail
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<10:
            score.highscore()
            snake.reset()

my_screen.exitonclick()
