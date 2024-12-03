from question import Question
from data import question_data
from quiz import Quiz
question_bank=[]
for i in question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quizz=Quiz(question_bank)

while quizz.still_has_questions():
    quizz.next_question()