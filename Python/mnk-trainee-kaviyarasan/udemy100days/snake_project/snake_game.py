import random
from turtle import Turtle, Screen
import time
import json

class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

        self.food = Turtle("circle")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.color("blue")
        self.food.speed("fastest")
        self.refresh_food()

        self.score = 0
        with open("data.json", "r") as data:
            self.high_score = json.load(data)

        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.goto(0, 270)
        self.scoreboard.hideturtle()
        self.update_scoreboard()

        self.screen.listen()
        self.screen.onkey(self.snake_up, "Up")
        self.screen.onkey(self.snake_down, "Down")
        self.screen.onkey(self.snake_left, "Left")
        self.screen.onkey(self.snake_right, "Right")

        self.run_game()

    def create_snake(self):
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            color = random.choice(colors)
            segment = Turtle("square")
            segment.color(color)
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)
        self.head = self.snake[0]

    def snake_reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
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
        high_scores = self.high_score["High score"]
        self.scoreboard.write(f"Score: {self.score}\n"
                              f"High Score1: {high_scores[0]}\n"
                              f"High Score2: {high_scores[1]}\n"
                              f"High Score3: {high_scores[2]}\n"
                              f"High Score4: {high_scores[3]}\n"
                              f"High Score5: {high_scores[4]}")
        self.scoreboard.goto(-260, 200)

    def reset(self):
        if self.score > self.high_score["High score"][-1]:
            self.high_score["High score"].append(self.score)
            self.high_score["High score"] = sorted(self.high_score["High score"],reverse= True)[:5]

            with open("data.json", "w") as data:
                json.dump(self.high_score, data, indent=4)

        self.score = 0
        self.update_scoreboard()

    def run_game(self):
        while True:
            self.screen.update()
            time.sleep(0.1)
            self.move()

            if self.head.distance(self.food) < 15:
                self.refresh_food()
                self.score += 1
                self.update_scoreboard()
                new_segment = Turtle("square")
                new_segment.color(random.choice(["red", "green", "blue", "yellow", "purple", "orange", "pink"]))
                new_segment.penup()
                self.snake.append(new_segment)
                last_segment = self.snake[-2]
                new_segment.goto(last_segment.xcor(), last_segment.ycor())

            if abs(self.head.xcor()) > 290 or abs(self.head.ycor()) > 290:
                self.reset()
                self.snake_reset()

            for segment in self.snake[1:]:
                if self.head.distance(segment) < 10:
                    self.reset()
                    self.snake_reset()


SnakeGame()

