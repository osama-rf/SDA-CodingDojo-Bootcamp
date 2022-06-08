from data import question_data
from test_class import Question
from quiz import Quiz

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.remaining_question():
    quiz.next_question()

print("You have comleted the quiz")
print(f"Your Final score was : {quiz.score} {quiz.question_number}")