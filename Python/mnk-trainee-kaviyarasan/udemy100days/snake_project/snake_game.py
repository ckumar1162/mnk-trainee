import random
from turtle import Turtle, Screen
import time

class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = []
        self.create_snake()


        self.food = Turtle("circle")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.color("blue")
        self.food.speed("fastest")
        self.refresh_food()

        # Scoreboard
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.goto(0, 270)
        self.scoreboard.hideturtle()
        self.update_scoreboard()

        # Control keys
        self.screen.listen()
        self.screen.onkey(self.snake_up, "Up")
        self.screen.onkey(self.snake_down, "Down")
        self.screen.onkey(self.snake_left, "Left")
        self.screen.onkey(self.snake_right, "Right")

        # Game loop
        self.run_game()

    def create_snake(self):
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            color = random.choice(colors)  # Select a random color from the list
            segment = Turtle("square")
            segment.color(color)
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x, y = self.snake[i - 1].position()
            self.snake[i].goto(x, y)
        self.head.forward(20)

    def snake_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snake_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def snake_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def refresh_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.food.goto(x, y)

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def run_game(self):
        while True:
            self.screen.update()
            time.sleep(0.1)
            self.move()

            # Detect food collision
            if self.head.distance(self.food) < 15:
                self.refresh_food()
                self.score += 1
                self.update_scoreboard()
                self.snake.append(Turtle("square"))

            # Detect wall collision
            if abs(self.head.xcor()) > 290 or abs(self.head.ycor()) > 290:
                self.game_over()
                break

            # Detect self collision
            for segment in self.snake[1:]:
                if self.head.distance(segment) < 10:
                    self.game_over()
                    break
SnakeGame()
