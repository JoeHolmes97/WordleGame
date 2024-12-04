
# This is a game where a random 5-letter word is picked from a list of them, and then you have to guess what it is,
# with correct letters being marked down, misplaced letters being shown as such and incorrect letters being shown as wrong.

# 1: Create an interface - Done
# 2: Have a label box for the word, initially populated with '_____', and have an input box where the user can type their guess
# 3: Import the 5-letter words as a tuple (as the imported words aren't going to change) and have the program pick on at random
# 4: When the user guesses have the program search the letters to see if any match the chosen word and tell the user if:
#   a: A letter isn't in the word
#   b: A letter is in the word but in the wrong place
#   c: A letter is in the word and in the right place
# 5: Limit the user to words that appear in the tuple (to stop a user just typing 'aaaaa') by throwing up an error if the word isn't in it
# 6: Limit the number of guesses a user can do before the game ends
# 7: Create a way to exit the game

from tkinter import *

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

introLabel = Label(window, text="Welcome to my wordle game! Please enter a 5-letter word to begin playing.")
introLabel.grid(row=0, column=0, columnspan=3)
# Create an introductory message and put it at the top of the screen

BlankLine(1,0)
# Create a blank space below the intro message
guessedLetters = "_____"
WordGuess(guessedLetters)

BlankLine(3,0)

textBox = Entry(window, width=50, borderwidth=5)
textBox.grid(row=4, column=0, columnspan=3)
# Create a text box for users to enter their gusses in

enterGuess = Button(window, text="Enter Guess", padx=10,pady=5)
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

window.mainloop()