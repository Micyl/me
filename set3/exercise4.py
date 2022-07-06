# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math
import random 

def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    
    # // is a "INTEGER DIVISION OPERATOR" meaning it will divide the
    # left value by the right and will keep the integer result - no need to cast to int

    # need a function to find median values per iteration

    # fuck with the bounds... ie, iterate down or up from the high/ low
    # can't seem to think of a way to test and increment atm...

    tries = 0
    guessed = False

    while not guessed:
        tries += 1
        guess = median(low, high)
        
        if guess == actual_number:
            guessed = True
            # just put the dictionary as the return. don't fuck about with creating it
            # earlier then having to return it from the function... 
            return {"guess": guess, "tries": tries}

        elif guess < actual_number:
            low = guess + 1
        
        elif guess > actual_number: 
            high = guess - 1



def median(low, high):
    median = (high + low) // 2
    return median



if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
