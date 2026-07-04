import random

# List of predefined words
words = ["python", "computer", "hangman", "coding", "program"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:

    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts Left:", attempts)

    # Check if player has guessed the word
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        attempts -= 1

# If attempts become 0
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)