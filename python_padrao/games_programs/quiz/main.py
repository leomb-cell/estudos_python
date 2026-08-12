from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# creating the question bank

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



newQ = QuizBrain(question_bank)

while newQ.stil_has_questions():
    newQ.next_question()
