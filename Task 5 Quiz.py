class Quiz:
    def __init__(self, questions):
        self.score = 0
        self.questions = questions
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def playQuiz(self):
        welcomeMessage = "Welcome to the Quiz Game! Please answer the following questions:"
        print(welcomeMessage)
        while self.questionIndex < len(self.questions):
            question = self.getQuestion()
            print(f"Q{self.questionIndex + 1}: {question.text}")
            for i, choice in enumerate(question.choices):
                print(f"{i+1}. {choice}")
            answer = input("Please enter your answer: ")
            self.guess(answer)
            self.loadQuestion()

        print(f"Your final score is: {self.score}")

    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {question.answer}")

    def loadQuestion(self):
        self.questionIndex += 1

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

# Define the quiz questions, choices, and answers
questions = [
    Question("Who is the current prime minister of India?", ["Narendra modi", "Rajeev Gandhi", "APJ Abdul Kalam","Sonia Gandhi"], "Narendra modi"),
    Question("What is the capital of Andhra Pradesh", ["Amaravathi", "Vijaywada", "Vizag","None of this"], "None of this"),
    Question("What is the square root of 36?", ["2", "4", "8","6"], "6")
]

# Start the quiz
quiz = Quiz(questions)
quiz.playQuiz()
