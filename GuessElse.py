#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.randint(1, 100)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))
        
        if x == guess:
            print("You genius!")
        else:
            if x > guess:
                print("Too low number!!.")
            else:
                print("Too high number!!.")

        

main()