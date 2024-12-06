class QuizzBrain:
    def __init__(self,q_list) :
        self.q_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_ques(self):
        if self.q_num < len(self.question_list):
            return True
        else:
            return False

    def next_ques(self):
        current_ques = self.question_list[self.q_num]
        self.q_num +=1
        user_answer = input(f"Q.{self.q_num}:{current_ques.text} (True/False):")
        self.check_answer(user_answer,current_ques.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You are right!")
        else:
            print(f"OH no ,that's wrong,The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.q_num}")        
