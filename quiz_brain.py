class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_no_question(self):
        if self.question_number<len(self.question_list):
            return True

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number+=1
        choice = input(f"Q.{self.question_number}: {question.text} True/False: ")
        return choice


    def  checking_answer(self, choice, q_answer):
        if choice.lower() == q_answer.lower():
            self.score+=1
            print("Correct answer +1")
        else:
            print("Wrong answer")

            
