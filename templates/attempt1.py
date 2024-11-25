
questions = [
        {
            "question": "Which keyword is used to define a function in python?",
            "Choices": ["a) fun", "b) define", "c) def", "d)func"],
            "answer": "c"
        },
        {
            "question": "Which movie among the list below is a karate based movie?",
            "Choices": ["a) Hitman", "b) White House Down", "c)Cobra Kai", "d)Teen Wolf"],
            "answer": "c"
        },
        {
            "question": "Who is your python instructor?",
            "Choices": ["a) James", "b) Charles", "c) William", "d) Abraham"],
            "answer": "b"
        }
    ]

def mock_quiz(question):
    print("Welcome to the mock quiz")
    print("Please answer the following questions")

    score = 0

    for question in questions:
        print(question["question"])

        for choice in question["Choices"]:
            print(f"{choice}")

        answer = input("Enter your answer: ")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    return score

def main():
    mock_quizzes = 3
    final_score = 0

    for i in range(mock_quizzes):
        print(f"--- Starting Quiz {i+1} ---")
        quiz_score = mock_quiz(questions)
        final_score += quiz_score

        print("\n--- Results ---")
        print(f"Quiz complete! Your score is {quiz_score}/{len(questions)}")
        play_again = input("\nWould you like to play again? (yes/no):").strip().lower()
        if play_again != 'yes':
            break

    print("\n--- Overall Statistics ---")
    print(f"\nOverall total score: {final_score}/{len(questions) * mock_quizzes}")

if __name__ == "__main__":
    main()

