import random
from pyscript import document

QUESTIONS = [
    {
        "snippet": "Bad things it's a lot of bad things...",
        "answer": "Gods Plan",
        "hint": "Released in 2018",
    },
    {
        "snippet": "Why you gotta fight with me at Cheesecake?",
        "answer": "Childs Play",
        "hint": "It's from Views",
    },
]

questions = QUESTIONS.copy()
random.shuffle(questions)

current_question = 0
score = 0


def normalize(text):
    return "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )


def show_question():
    question = questions[current_question]

    document.querySelector("#question").innerText = (
        question["snippet"]
    )


def check_answer(event=None):
    global current_question, score

    user_answer = document.querySelector("#answer").value

    question = questions[current_question]

    if normalize(user_answer) == normalize(question["answer"]):
        score += 1
        document.querySelector("#result").innerText = "✅ Correct!"
    else:
        document.querySelector("#result").innerText = (
            f"❌ The answer was {question['answer']}"
        )

    document.querySelector("#score").innerText = (
        f"Score: {score}/{current_question + 1}"
    )

    current_question += 1

    if current_question < len(questions):
        document.querySelector("#answer").value = ""
        show_question()
    else:
        document.querySelector("#question").innerText = (
            "🎉 Game finished!"
        )


document.querySelector("#submit").addEventListener(
    "click",
    check_answer
)

show_question()
