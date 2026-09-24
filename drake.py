import random

QUESTIONS = [
    {
        "snippet": "Bad things it's a lot of bad things that they wishin' and wishin'And wishin' and wishin', they wishin' on me",
        "answer": "Gods Plan",
        "hint": "Released in 2018",
    },
    {
        "snippet": "Oti Oti, there's never much love when we go OT I __ to make it back in one piece, I pray, I pray",
        "answer": "One Dance",
        "hint": "A dancehall-influenced hit",
    },
    {
        "snippet": "Ever since I left the city, you got a reputation for yourself now everybody knows and I feel left out",
        "answer": "Hotline Bling",
        "hint": "Known for its distinctive music video",
    },
    {
        "snippet": "First time I saw ya you wouldn't give me time of day now that I know ya I probably should've walked away",
        "answer": "Princess",
        "hint": "Related to Drakes new partner ",
    },
    {
        "snippet": "But I was curious and Ill never forget it, baby, what an experience you could've been the one, but it wasn't that serious",
        "answer": "Fireworks",
        "hint": "it's in the album thank me later",
    },
    {
        "snippet" : "I, I, I, I, I, I think I'd lie for you, I think I'd die for you",
        "answer" : "controlla",
        "hint" : " jonaci",
    },
    {
        "snippet" : """Listen, Seeing you got ritualistic, Cleansin' my soul of addiction for now
\'Cause I\'m fallin' apart
Yeah, tension""",
        "answer" : "Passionfruit",
        "hint" : " ",
    },
    {
        "snippet" : "Why you gotta fight with me at Cheesecake? You know I love to go there Say I'm actin' lightskin, I can't take you nowhere",
        "answer" : "Childs Play",
        "hint" : "he's known for this",
        
    
}]


def normalize(text):
    """Make answers easier to compare."""
    return "".join(character.lower() for character in text if character.isalnum())


def play_game():
    print("🎵 Drake Lyrics Game 🎵")
    print("Guess the song from the lyric snippet.")
    print("Type 'quit' at any time to exit.\n")

    questions = QUESTIONS.copy()
    random.shuffle(questions)

    score = 0

    for number, question in enumerate(questions, start=1):
        print(f"Question {number}/{len(questions)}")
        print(f'Lyric: "{question["snippet"]}"')

        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == "quit":
            break

        if normalize(user_answer) == normalize(question["answer"]):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Not quite. The answer was: {question['answer']}")
            print(f"Hint: {question['hint']}\n")

    print(f"Game over! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    play_game()
