
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




window.mainloop()