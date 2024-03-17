class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, options, correct_answer):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter your choice: ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer = int(user_answer)
            if options[user_answer - 1] == correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
        else:
            print("Invalid choice. Please enter a number corresponding to your choice.")

    def run_quiz(self):
        for question, options, correct_answer in self.questions:
            self.ask_question(question, options, correct_answer)
        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


def main():
    questions = [
        ("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"),
        ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
        ("What is the powerhouse of the cell?", ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic reticulum"], "Mitochondria")
    ]
    quiz = Quiz(questions)
    quiz.run_quiz()


if __name__ == "__main__":
    main()
