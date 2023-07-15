import random

hangman_stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''',

    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',

    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',

    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',

    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',

    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',

    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

words = {
    "car": "You drive around",
    "tree": "It has leaves",
    "banana": "A yellow fruit",
    "computer": "An electronic device",
    "dog": "A loyal pet",
    "pizza": "A popular food",
    "guitar": "A musical instrument",
    "beach": "A sandy shoreline",
    "sunflower": "A tall, yellow flower",
    "book": "Contains stories and information",
    "mountain": "A large natural elevation",
    "ocean": "A vast body of saltwater",
    "football": "A popular sport",
    "rainbow": "A colorful arc in the sky",
    "piano": "A musical instrument with keys",
    "butterfly": "An insect with colorful wings",
    "coffee": "A popular caffeinated beverage",
    "moon": "Earth's natural satellite",
    "fireworks": "Explosive displays of light and color",
    "painting": "An artistic creation on canvas"
}


def get_random_word():
    return random.choice(list(words.keys()))


def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
        displayed += " "
    return displayed


def play_hangman():
    word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("*" * 15, "Hangman Game", "*" * 15)
    print(display_word(word, guessed_letters))
    print("Hint:", words[word])

    while incorrect_guesses < len(hangman_stages) - 1:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(hangman_stages[incorrect_guesses])

        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word correctly!")
            break

    if "_" in display_word(word, guessed_letters):
        print("You ran out of guesses. The word was:", word)


play_hangman()
