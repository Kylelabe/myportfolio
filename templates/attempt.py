# myName = input("Enter your name: ")
# favColor = input("Enter your favorite color: ")
#
# print(f"Hello,{myName}! Your favorite color is: {favColor}")

def run_quiz(questions):
    print("Welcome to python and movies quiz!")
    print("Answer the following questions by typing the letter of your choice:(a, b, c, d).\n")
    score = 0
    for question in questions:
       print(question["question"])
       for choice in question["Choices"]:
          print(f"{choice}")

       answer = input("Enter your answer: ")
       if answer == question["answer"]:
         print("Correct!")
         score += 1
       else: print("Incorrect!")

    return score

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


def main():
    total_score = 0
    number_of_quizzes = 3

    for i in range(number_of_quizzes):  # Run the quiz 3 times
        print(f"\n--- Starting Quiz {i+1} ---")
        quiz_score = run_quiz(questions)
        total_score += quiz_score

        print("\n--- Results ---")
        print(f"Quiz complete! Your score is {quiz_score}/{len(questions)}")
        play_again = input("\nWould you like to play again? (yes/no):").strip().lower()
        if play_again != 'yes':
            break


    print("\n--- Overall Statistics ---")
    print(f"\nOverall total score: {total_score}/{len(questions) * number_of_quizzes}")


if __name__ == "__main__":
    main()



    # qn = {
    #     "What is the capital of Kenya?":
    #         "Nairobi",
    # }
    # while True:
    #     score = 0
    #     print("\n Welcome to the Quiz game!:video_game:")
    #
    #     for qn, answer in qn.items():
    #         user_answer = input(f"\n {qn}.")