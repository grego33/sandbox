import random

random_words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "ugli",
    "watermelon",
]

# 1. choose a random word from a list of words
word = random_words[random.randint(0, len(random_words)-1)]

answer = []
for i in range(0, len(word)):
    answer += "?"

def print_game_state():
    print(answer)
    print(f"Guesses left: {strikes}")

strikes = 6

while (word != ''.join(answer) and strikes > 0):
    print_game_state()
    guess = input("Guess a letter (lower case): ")
    guessed = False
    i = 0
    while (not(guessed) and i < len(word)):
        if (guess == word[i] and answer[i] == '?'):
            answer[i] = word[i]
            guessed = True

        i += 1

    if not(guessed):
        strikes -= 1

if (word != ''.join(answer)):
    print(f"You lose!  It was {word}")
else:
    print(f"Yay, you won!")