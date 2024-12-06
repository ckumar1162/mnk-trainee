from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank =[]
for question in question_data:
    quizz_question = question["text"]
    quizz_answer = question["answer"]
    new_question = Question(quizz_question,quizz_answer)
    question_bank.append(new_question)


quizz = QuizzBrain(question_bank)
while quizz.still_has_ques:
    quizz.next_ques()   


print(f"Congrats! You have completed the quizz and ur final score is {quizz.score}/{quizz.q_num}")    