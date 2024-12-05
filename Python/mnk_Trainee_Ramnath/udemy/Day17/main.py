from data import question_data
import question_model
import quiz_brain

# TODO: creating the list of question object from Data
question_bank=[]

for i in question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    new_quest=question_model.Question(question_text,question_answer)
    question_bank.append(new_quest)

qbank=quiz_brain.QuizBrain(question_bank)

while qbank.is_still_has_quest():
     qbank.next_question()
print("/n")
print("You have completed quiz")
print(f"Your final score is : {qbank.score}/{qbank.question_number}")