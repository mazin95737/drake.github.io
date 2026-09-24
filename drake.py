import random
from pyscript import document


QUESTIONS = [
    {
        "snippet": "Bad things it's a lot of bad things that they wishin' and wishin' And wishin' and wishin', they wishin' on me",
        "answer": "Gods Plan",
        "hint": "Released in 2018",
    },

    {
        "snippet": "Oti Oti, there's never much love when we go OT I __ to make it back in one piece, I pray, I pray",
        "answer": "One Dance",
        "hint": "A dancehall-influenced hit",
    },

    {
        "snippet": "Ever since I left the city, youbgot a reputation for yourself now everybody knows and I feel left out",
        "answer": "Hotline Bling",
        "hint": "Known for its distinctive music video",
    },

    {
        "snippet": "First time I saw ya you wouldn't give me time of day now that I know ya I probably should've walked away",
        "answer": "Princess",
        "hint": "Related to Drake's new partner",
    },

    {
        "snippet": "But I was curious and Ill never forget it, baby, what an experience you could've been the one, but it wasn't that serious",
        "answer": "Fireworks",
        "hint": "It's in the album Thank Me Later",
    },

    {
        "snippet": "I, I, I, I, I, I think I'd lie for you, I think I'd die for you",
        "answer": "Controlla",
        "hint": "From Views",
    },

    {
        "snippet": """Listen, Seeing you got ritualistic, Cleansin' my soul of addiction for now
'Cause I'm fallin' apart
Yeah, tension""",
        "answer": "Passionfruit",
        "hint": "From More Life",
    },

    {
        "snippet": "Why you gotta fight with me at Cheesecake? You know I love to go there Say I'm actin' lightskin, I can't take you nowhere",
        "answer": "Childs Play",
        "hint": "From Views",
    },
]


# -------------------------
# GAME VARIABLES
# -------------------------

questions = QUESTIONS.copy()

random.shuffle(questions)

current_question = 0
score = 0
answered = False


# -------------------------
# NORMALIZE ANSWERS
# -------------------------

def normalize(text):
    return "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )


# -------------------------
# SHOW QUESTION
# -------------------------

def show_question():
    global answered

    answered = False

    question = questions[current_question]

    document.querySelector("#question-number").innerText = (
        f"Question {current_question + 1}/{len(questions)}"
    )

    document.querySelector("#lyrics").innerText = (
        f'"{question["snippet"]}"'
    )

    document.querySelector("#result").innerText = ""

    document.querySelector("#hint").innerText = ""

    document.querySelector("#answer").value = ""

    document.querySelector("#submit").style.display = "inline-block"

    document.querySelector("#hint-button").style.display = "inline-block"

    document.querySelector("#next-button").style.display = "none"

    document.querySelector("#score").innerText = (
        f"Score: {score}/{len(questions)}"
    )


# -------------------------
# CHECK ANSWER
# -------------------------

def check_answer(event=None):
    global score
    global answered

    if answered:
        return

    user_answer = document.querySelector("#answer").value

    if not user_answer.strip():
        document.querySelector("#result").innerText = (
            "⚠️ Please enter an answer!"
        )

        return

    question = questions[current_question]

    if normalize(user_answer) == normalize(question["answer"]):

        document.querySelector("#result").innerText = (
            "✅ Correct!"
        )

        score += 1

    else:

        document.querySelector("#result").innerText = (
            f"❌ Not quite! The answer was: {question['answer']}"
        )

    answered = True

    document.querySelector("#score").innerText = (
        f"Score: {score}/{len(questions)}"
    )

    document.querySelector("#submit").style.display = "none"

    document.querySelector("#next-button").style.display = "inline-block"


# -------------------------
# SHOW HINT
# -------------------------

def show_hint(event=None):

    question = questions[current_question]

    document.querySelector("#hint").innerText = (
        f"💡 Hint: {question['hint']}"
    )


# -------------------------
# NEXT QUESTION
# -------------------------

def next_question(event=None):
    global current_question

    current_question += 1

    if current_question >= len(questions):

        end_game()

        return

    show_question()


# -------------------------
# END GAME
# -------------------------

def end_game():

    percentage = round(
        (score / len(questions)) * 100
    )

    document.querySelector("#question-number").innerText = (
        "🎉 Game Complete!"
    )

    document.querySelector("#lyrics").innerText = (
        f"You scored {score}/{len(questions)}!"
    )

    document.querySelector("#result").innerText = (
        f"That's {percentage}%!"
    )

    document.querySelector("#hint").innerText = (
        "Thanks for playing 🎵"
    )

    document.querySelector("#submit").style.display = "none"

    document.querySelector("#hint-button").style.display = "none"

    document.querySelector("#next-button").style.display = "none"


# -------------------------
# RESTART GAME
# -------------------------

def restart_game(event=None):
    global questions
    global current_question
    global score

    questions = QUESTIONS.copy()

    random.shuffle(questions)

    current_question = 0
    score = 0

    show_question()


# -------------------------
# CONNECT BUTTONS
# -------------------------

document.querySelector("#submit").addEventListener(
    "click",
    check_answer
)

document.querySelector("#hint-button").addEventListener(
    "click",
    show_hint
)

document.querySelector("#next-button").addEventListener(
    "click",
    next_question
)

document.querySelector("#restart").addEventListener(
    "click",
    restart_game
)


# Start the game
show_question()
