
# This is a game where a random 5-letter word is picked from a list of them, and then you have to guess what it is,
# with correct letters being marked down, misplaced letters being shown as such and incorrect letters being shown as wrong.

# 1: Create an interface - Done
# 2: Have a label box for the word, initially populated with '_____', and have an input box where the user can type their guess - Done
# 3: Import the 5-letter words as a tuple (as the imported words aren't going to change) and have the program pick one at random - Done 
# 4: When the user guesses have the program search the letters to see if any match the chosen word and tell the user if:
#   a: A letter isn't in the word
#   b: A letter is in the word but in the wrong place
#   c: A letter is in the word and in the right place
# 5: Limit the user to words that appear in the tuple (to stop a user just typing 'aaaaa') by throwing up an error if the word isn't in it
# 6: Limit the number of guesses a user can do before the game ends
# 7: Create a way to exit the game

import random
from tkinter import *

from random import randint as randint

window = Tk()

window.title("Wordle Game")

def BlankLine(row, column):
    blankSpace = Label(window, text="")
    blankSpace.grid(row=row, column=column, columnspan=3)
# A function for creating a blank line in the window

def WordGuess(guessedLetters):
    
    guessedLetters = Label(window, text="| " + guessedLetters + " |")
    guessedLetters.grid(row=2, column=1)
# A function for creating a label to show the guessed letters

def guessingWord(randomWord, wordList, errorMessage):
# Function for taking the users guess and comparing it to the random word, covering the errors users might make
    guessInput = textBox.get()
    
    message = ""
    
    errorMessage.forget()
    # Forget (clear) the space where the label is whenever this function is called

    if guessInput.isalpha() == False:
        message = "Sorry, the text you just entered contains something that is not a letter. Please try again."
        # If the user input contains non-letter character, throw up an error message.

    elif len(guessInput) != 5:
        message = "I'm sorry, the word you just entered was not 5 letters. Please try again."
        # If the user input is less than 5 letters or greater than 5 letters, throw up an error message.

    elif (guessInput.lower() + "\n") not in wordList:
        message = "Sorry, the word you just entered is not in my dictionary. Please try again."

    else:
        message = ""
        ComparingWord(randomWord, guessInput)
        return guessInput

    errorMessage.config(text=message)
    # Edit the errorMessage label, changing the text to the variable given

def ComparingWord(randomWord, guessInput):
    return


introLabel = Label(window, text="Welcome to my wordle game! Please enter a 5-letter word to begin playing.")
introLabel.grid(row=0, column=0, columnspan=3)
# Create an introductory message and put it at the top of the screen

wordList = tuple(open("Words.txt", "r"))
# Reads the words.txt file into a tuple, but has "\n" at the end of every word because I don't know how to remove it

randomWord = wordList[randint(0,(len(wordList)))]

print(randomWord)

BlankLine(1,0)
# Create a blank space below the intro message

guessedLetters = "_____"
WordGuess(guessedLetters)
# Use the WordGuess function to display a default text label


errorMessage = Label(window, text="")
errorMessage.grid(row=3, column=0, columnspan=3)
# Create a label for the errors that could happen

textBox = Entry(window, width=50, borderwidth=5)
textBox.grid(row=4, column=0, columnspan=3)
# Create a text box for users to enter their gusses in

enterGuess = Button(window, text="Enter Guess", padx=10,pady=5, command=lambda: guessingWord(randomWord, wordList, errorMessage))
enterGuess.grid(row=5,column=1)
# Create a button for entering the guess

BlankLine(6,0)

correctLettersTitle = Label(window, text="Correct Letters")
correctLettersTitle.grid(row=7,column=0)
misplacedLettersTitle = Label(window, text="Misplaced Letters")
misplacedLettersTitle.grid(row=7,column=1)
incorrectLettersTitle = Label(window, text="Incorrect Letters")
incorrectLettersTitle.grid(row=7,column=2)
# Create titles for the section where the used letters will go

correctLetters = Text(window, height=8, width=15)
correctLetters.grid(row=8, column=0)

misplacedLetters = Text(window, height=8, width=15)
misplacedLetters.grid(row=8, column=1)

incorrectLetters = Text(window, height=8, width=15)
incorrectLetters.grid(row=8, column=2)


window.mainloop()