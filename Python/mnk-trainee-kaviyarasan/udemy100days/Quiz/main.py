from data import question_data
from question_model import Question
from quiz_brain import Quizbrin
question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Quizbrin(question_bank)

while quiz.still_has_questions():
    quiz.next_questions()

print("you completed quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")
