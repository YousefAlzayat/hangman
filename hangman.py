import random
from word_dict import word_list
from stages import game_stages
import time



# This function calls a random word from the word dictionary
def get_word():
    global word
    word = random.choice(word_list).upper()
    print(word)

# This is the game ending function
def endgame():
    print("This program will terminate in 5 seconds")
    time.sleep(5)

# This is the main game function
def game(word):

    guesses = 7
    guessed_letters = []
    guessed_words = []
    remaining_letters = len(word)

    # Main game loop
    while True:

        # To check if user has run out of guesses
        if guesses == 0:
            print("You lost the game, The word was", word)
            time.sleep(1)
            endgame()
            break

        # used to print the drawing of the hangman and the blank letters and guessed letters
        print(game_stages[guesses-1])
        game_blanks = ""
        for i in word:
            if i in guessed_letters:
                game_blanks = game_blanks + i
            else:
                game_blanks = game_blanks + "_"
        print(game_blanks)
        print("\n" * 10)

        # Asks for the user's guess
        guess = input("Please guess a letter or a word: ").upper()

        # Checking if the input string is inside the word
        if guess in word:

            # If the guess was a letter
            if len(guess) == 1:

                # Checks if the letter was already guessed
                if guess in guessed_letters:
                    print("You already guessed that letter, Try again.")

                else:
                    guessed_letters.append(guess)
                    for letter in word:
                        if letter == guess:
                            remaining_letters = remaining_letters - 1

                    # In case this was the last letter remaining
                    if remaining_letters == 0:
                        print("Congrats, You guessed the word:", word)
                        time.sleep(1)
                        endgame()
                        break

                    # In case the letter was correct but not the last one remaining
                    if remaining_letters > 0:
                        print("That's right the letter", guess, "is in the word.")

            # In case it's the correct word
            elif len(guess) == len(word):
                print("That's right,", guess, "is the word.")
                time.sleep(1)
                print("Thank you for playing!")
                time.sleep(1)
                endgame()
                break

            # If neither a letter nor a word of the same length print an error message
            else:
                print("Please enter either a letter or a word.")

        # If not in the word
        else:

            # If it was a letter and not in the word
            if len(guess) == 1:
                if guess in guessed_letters:
                    print("You already guessed that letter, Try again.")
                else:
                    guessed_letters.append(guess)
                    print("The letter", guess, "is not in the word.")
                    guesses -= 1

            # If it was a word with the same length and not the word
            elif len(guess) == len(word):
                if guess in guessed_words:
                    print("You already guessed that word, Try again.")
                else:
                    guessed_words.append(guess)
                    print(guess, "is not the word.")
                    guesses -= 1

            # If it was neither a letter nor a word of the same length
            else:
                print("Please enter either a letter or a word.")


get_word()
game(word)
