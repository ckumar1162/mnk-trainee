from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day20_code\data.txt") as fp:
            self.high_score = int(fp.read())
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} HighScore = {self.high_score}",align="center",font=("Arial",20,"normal"))

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER....  (0_0)",align="center",font=("Arial",20,"normal"))

    def highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day20_code\data.txt",mode="w") as fp:
                fp.write(f"{self.high_score}")
            self.score = 0
        self.update_score()

           

    def increase_score(self):
        self.score +=1
        self.update_score()
