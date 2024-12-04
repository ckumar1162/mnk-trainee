class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def is_still_has_quest(self):
        return self.question_number<len(self.question_list)

    def check_ans(self,choice,c_ans):
        if choice.lower()==c_ans.lower():
            self.score +=1
            print("You got it Right")

        else:
            print("that's wrong")
        print(f"Correct answer is : {c_ans}")
        print(f"Your score : {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_quest=self.question_list[self.question_number]
        self.question_number +=1
        choice_ans=input(f"Q {self.question_number}.: {current_quest.text} (True/False)?")
        self.check_ans(choice_ans,current_quest.answer)
