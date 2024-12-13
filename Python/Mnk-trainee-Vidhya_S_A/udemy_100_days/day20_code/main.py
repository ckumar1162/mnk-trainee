#snake game using turtle and oops concept
from turtle import Turtle,Screen
from snake_game import SnakeGame
import time


my_screen = Screen()
my_screen.bgcolor("olive")
my_screen.setup(600,600)
my_screen.title("Snake game")
my_screen.tracer(0) #tracer() is used to control the speed of the drawing or toggle the animation  of the turtle movement



snake = SnakeGame()
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
    time.sleep(0.1)
    
    snake.move_snake()   





my_screen.exitonclick()
