"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

# def super_asker(low, high):
#     """Robust asking function.

#     Combine what you learnt from stubborn_asker and not_number_rejector
#     to make a function that does it all!
#     Try to call at least one of the other functions to minimise the
#     amount of code.
#     """
#     while True:
#         try:
#             the_input = input(f"Insert a number between {low} and {high}: ")
#             our_number = int(the_input) 
#             if our_number >= low and our_number <= high:
#                 return our_number           
#             else:
#                 print("that number is out of bounds")
#         except:
#             print("that wasn't a number")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print('Welcome to the Advanced Guessing Game!')
    print('You will need to guess a number between a range of numbers of YOUR choosing.')
    lower_bound = int(input('Set the lowest, starting number: '))
    upper_bound = int(input("Set the highest, end number of your range: "))
    print('Fantastic - we will be guessing a number between {} and {}! Good Luck!'.format(lower_bound, upper_bound))

    # "randint" must need to be used as to not get float random number ? 
    real_number = random.randint(lower_bound, upper_bound)
    
    guessed = False

    while not guessed:
        try:
            # needs to be inside the 'try' for the except to function 
            guessed_number = int(input('Input a number to begin: '))
            print('You have guessed {}!'.format(guessed_number))    
            if guessed_number == real_number:
                print('No way - you got it! Well Done!')
                guessed = True
            elif guessed_number < lower_bound and real_number:
                print('Not a very bright one are we... I mean, you chose the numbers!!! Try Again...')
            elif guessed_number > upper_bound and real_number:
                print('You absolute nonce... Why would the number be ousite of what you have set??? Try Again...')
            elif guessed_number < real_number and guessed_number > lower_bound:
                print('Way too small dude!')
            elif guessed_number > real_number and guessed_number < upper_bound:
                print('Way over the top, a bit less perhaps?')
            
        except:
            print('Erm... thats not a number... ')
        
        # TO DO:
        # Continue looking into type error handling... 
        # ie, steer user error via feedback on input type 



    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
