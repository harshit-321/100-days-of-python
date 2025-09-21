print("********************")
print("Welcome to my Quiz Game!!!")

question_bank = [
    "The ability of one class to acquire methods and attributes of another class is called ___.",
    "Which of the following is a type of inheritance?",
    "What type of inheritance has multiple subclasses to a single superclass?",
    "What is the depth of multilevel inheritance in python?",
    "What does MRO stands for?"
]

answers = ["A", "D", "C", "C", "B"]

options = [["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
           ["A. Single", "B. Double", "C. Multiple", "D. both A and B"],
           ["A. Multiple Inheritance", "B. MultiLevel Inheritance", "C. Hierarchical inheritance", "D. None of these"],
           ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
           ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order",
            "D. Method Resolution Object"]
           ]
score = 0
question_num = 0
for each_question in question_bank:
    print("*******************")
    print(each_question)

    for i in options[question_num]:
        print(i)

    guess = input("Enter your answer(A/B/C/D): ").upper()

    if guess == answers[question_num]:
        print("Correct")
        score += 1

    else:
        print("Incorrect")
        print(f"the correct answer is: {answers[question_num]}")
    question_num += 1

    print(f"your score is: {score}/{(question_num)}")
    print(f"Final score is {score}")
    print(f"score is {(score / len(question_bank)) * 100}%")

