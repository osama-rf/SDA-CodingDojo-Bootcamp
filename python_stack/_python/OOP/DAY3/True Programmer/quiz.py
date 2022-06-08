class Quiz:
    def __init__(self, quiz_list):
        self.question_number = 0
        self.score = 0
        self.question_list = quiz_list


def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"{self.question_number}: {current_question.question} (Mulitple Choice): ")
    self.check_answer(user_answer, current_question.answer)


def remaining_question(self):
    return self.question_number < len(self.question_list)


def check_answer(self, user_answer, answer):
    if user_answer == answer:
        self.score += 1
        print("Hmmm, Your Are Right Dude ;)")
    else:
        print("Awesome, Youe Should find another Job")

    print(f"The correct answer was: {answer}")
    print(f"Your current score is: {self.score}/{self.question_number}\n")