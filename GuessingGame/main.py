from Question import Question

# Quessing Game
print("=== Welcome to My Guessing Game ===\n")

# list of questions
question_prompts =[
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# list of questions to be asked in order
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0;

    for question in questions:  # for-each loop thru questions[]
        user_answer = input(question.prompt)
        if user_answer == question.answer:  # if user answer is == to actual answer
            score += 1

    print("You got " + str(score) + " / " + str(len(questions)) + " correct!")

run_test(questions)
