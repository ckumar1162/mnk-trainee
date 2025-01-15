from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ('arial',15,'italic') 
class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain 
        self.window = Tk()
        self.window.title('Quizz Game')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = Label(text='Score:0',fg = 'white',bg=THEME_COLOR,font=FONT)
        self.score.grid(column=1,row=0)

        self.canvas = Canvas(width=400,height=300,bg='white')
        self.question_text = self.canvas.create_text(200,150,width=380,text="Some text",fill='black',font=FONT)
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        self.right_img = PhotoImage(file=r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\quizzler-app-start\images\true.png')
        self.right_button = Button(image=self.right_img,highlightthickness=0,command=self.right)
        self.right_button.grid(column=1,row=2)

        self.wrong_img = PhotoImage(file=r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\quizzler-app-start\images\false.png')
        self.wrong_button = Button(image=self.wrong_img,highlightthickness=0,command=self.wrong)
        self.wrong_button.grid(column=2,row=2)


        self.get_next_question()






        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score.config(text=f'Score : {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f'You reached and your score is {self.quiz.score}')    

    def right(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
    def wrong(self):
        is_right =self.quiz.check_answer("False")
        self.feedback(is_right)
                    
    def feedback(self,is_right): 
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)                       