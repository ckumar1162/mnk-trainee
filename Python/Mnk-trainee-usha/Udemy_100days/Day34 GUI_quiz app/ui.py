from tkinter import *
from quiz_brain import QuizBrain
#import csv
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            # self.save_score()
            # self.display_scoreboard()
            self.canvas.itemconfig(self.question_text,text="you have reached end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

    # def save_score(self):
    #     """Save the current player's score to a file."""
    #     name = self.get_player_name()
    #     with open(SCOREBOARD_FILE, mode="a", newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow([name, self.quiz.score])
    #
    # def get_player_name(self):
    #     """Prompt the user to enter their name."""
    #     name = self.window.simpledialog.askstring("Name", "Enter your name:")
    #     return name if name else "Anonymous"
    #
    # def display_scoreboard(self):
    #     """Display the top 3 scores from the scoreboard."""
    #     scores = self.load_scores()
    #     top_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:3]
    #     scoreboard_text = "Top Scores:\n" + "\n".join([f"{name}: {score}" for name, score in top_scores])
    #     self.canvas.itemconfig(self.question_text, text=scoreboard_text)
    #
    # def load_scores(self):
    #     """Load scores from the scoreboard file."""
    #     scores = []
    #     try:
    #         with open(SCOREBOARD_FILE, mode="r") as file:
    #             reader = csv.reader(file)
    #             scores = [(row[0], int(row[1])) for row in reader]
    #     except FileNotFoundError:
    #         pass
    #     return scores