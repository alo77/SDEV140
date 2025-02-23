"""
Program: Module 06 Practice Exercise 9-5
Author: Abigail Logan
Date: 02/24/2025
Short Description: This program is a number guessing game where the computer tries to guess a number between 1 and 100. It uses the breezypythongui library to create a simple window with buttons that let you say if the guess is too small, too large, or correct.
"""

from breezypythongui import EasyFrame # type: ignore

class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Guessing Game")
        self.lower = 1
        self.upper = 100
        self.guess = (self.lower + self.upper) // 2
        self.addLabel("Guess a number between 1 and 100", row = 0, column = 0, columnspan = 2)
        self.guessLabel = self.addLabel (text="My guess is " + str(self.guess), row = 1, column = 0, columnspan = 2)
        self.addLabel("Your guess: ", row = 1, column = 0)
        self.addTextField("0", row = 1, column = 1)
        self.addButton("Too Small", row = 2, column = 0)
        self.addButton("Too Large", row = 2, column = 1)
        self.addButton("Correct", row = 3, column = 0, columnspan = 2)
        self.addButton("New Game", row = 4, column = 1)
        self.addButton("Quit", row = 4, column = 0, columnspan = 2)
    
    def tooSmall(self):
        self.lower = self.guess
        self.guess = (self.lower + self.upper) // 2
        self.guessLabel.setText("My guess is " + str(self.guess))
    
    def tooLarge(self):
        self.upper = self.guess
        self.guess = (self.lower + self.upper) // 2
        self.guessLabel.setText("My guess is " + str(self.guess))
    
    def correct(self):
        self.guessLabel.setText("I guessed it! The number was " + str(self.guess))
    
    def newGame(self):
        self.lower = 1
        self.upper = 100
        self.guess = (self.lower + self.upper) // 2
        self.guessLabel.setText("My guess is " + str(self.guess))
    
    def quit(self):
        self.close()

def main():
    GuessingGame().mainloop

if __name__ == "__main__":
    main()