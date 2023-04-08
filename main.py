import random
import nltk
import os

# Download the words corpus if necessary
nltk.download('words')

# Get a list of words from the words corpus
word_list = nltk.corpus.words.words()

# Select a random word from the list
word = random.choice(word_list)

# Function to print the current state of the word with underscores for unguessed letters
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    print(displayed)

# Keep track of guessed letters and number of guesses remaining
guessed_letters = []
guesses_remaining = 6

# Game loop
while True:
    os.system("cls")
    print("\nGuess the word:")
    display_word(word, guessed_letters)
    print("Guessed letters:", guessed_letters)
    print("Guesses remaining:", guesses_remaining)

    # Ask for a letter guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter and not already guessed
    if len(guess) != 1:
        print("Please guess a single letter.")
        continue
    elif guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in word:
        print("Correct!")
    else:
        print("Incorrect.")
        guesses_remaining -= 1

    # Check if the game is over
    if set(word) <= set(guessed_letters):
        print("You win! The word was", word)
        break
    elif guesses_remaining == 0:
        print("Game over! The word was", word)
        break
