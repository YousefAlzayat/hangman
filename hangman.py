import random
from word_dict import word_list
from stages import game_stages
import time


## This function calls a random word from the word dictionary

def get_word():
    global word
    word = random.choice(word_list).upper()


## This is the game ending function

def endgame():
    global guessed
    guessed = True
    print("That's right, you guessed the word,", word)
    time.sleep(1)
    print("Thank you for playing!")
    time.sleep(1)
    print("This program will terminate in 5 seconds")
    time.sleep(5)


## This is the main game function

def game(word):


    guessed = False
    guessed_letters = []
    guessed_words = []
    letter_counter = 0
    remaining_letters = len(word)
    guesses = 7


    while guessed == False:

        print(game_stages[guesses-1])
        game_blanks = ""
        for i in word:
            if i in guessed_letters:
                game_blanks = game_blanks + i
            else:
                game_blanks = game_blanks + "_"
        print(game_blanks)
        print("\n")




        guess = input("Please guess a letter or a word: ").upper()

        if guess in word:
            if len(guess) == 1:
                for letter in word:
                    if letter == guess:
                        remaining_letters = remaining_letters - 1
                if remaining_letters == 0:
                    endgame()
                    break
                if remaining_letters > 0:
                    print("That's right the letter", guess, "is in the word.")
                    guessed_letters.append(guess)

            elif len(guess) == len(word):
                guessed_words.append(guess)
                print("That's right,", guess, "is the word.")
                guessed = True
                time.sleep(1)
                print("Thank you for playing!")
                time.sleep(1)
                print("This program will terminate in 5 seconds")
                time.sleep(5)
                break
            else:
                print("Please enter either a a letter or a word.")



        else:
            if len(guess) == 1:
                if guess in guessed_letters:
                    print("You already guessed that letter, Try again.")
                else:
                    guessed_letters.append(guess)
                    print("The letter", guess, "is not in the word.")
                    guesses -= 1
            elif len(guess) == len(word):
                if guess in guessed_words:
                    print("You already guessed that word, Try again")
                else:
                    guessed_words.append(guess)
                    print(guess, "is not the word.")
                    guesses -= 1
            else:
                print("Please enter either a letter or a word.")


        if guesses == 0:
            print("You lost the game, The word was", word)
            time.sleep(1)
            print("The program will terminate in 5 seconds")
            time.sleep(5)
            guessed = True
            break
get_word()
game(word)
