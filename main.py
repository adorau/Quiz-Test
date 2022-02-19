from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain


n = 0
question_bank = []

for i in question_data:
    q_text = question_data[n]["text"]
    q_answer = question_data[n]["answer"]
    q = QuestionModel(q_text,q_answer)
    question_bank.append(q)
    n+=1

quiz = QuizBrain(question_bank)

while quiz.still_has_no_question():
    choice = quiz.next_question()
    question = quiz.question_list[quiz.question_number-1]
    quiz.checking_answer(choice,question.answer)

print(f"You've got {quiz.score}")


