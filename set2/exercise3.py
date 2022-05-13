# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""


from calendar import c
from distutils.command.build_scripts import first_line_re
from inspect import classify_class_attrs
from re import sub
from shutil import move
from textwrap import fill


def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even.

    Look into modulo division using the '%' operator as one way of doing this.
    """
    the_number_is = a_number % 2 == 1

    return the_number_is


def fix_it(moves=True, should_move=True):
    """Decide what to do.

    Using the engineering flowchart (in week2 folder of the CODE1161-2019
    repo engineeringFlowchart.png) for the rules, return the apropriate
    response to the input parameters.
    Use conditional statements: if, else, elif etc.
    This function should return either:
    "WD-40"
    "Duct Tape"
    "No Problem"

    Most people write this function with 4 return statements. 
    As an extra challenge, see if you can get that down to three.
    """
    if moves == should_move:
        return "No Problem"
    elif moves and not should_move:
        return "Duct Tape"
    elif should_move and not moves:
        return "WD-40"


    # if moves == should_move:
    #     return "No Problem"
    #     # combine operators to do something. 

    #     # "else, if it moves AND [is NOT] or 
    #     # [opposite of condition to should_move] should NOT move"

    #     # the NOT is inversing the boolean? 
    # elif moves and not should_move:
    #     return "Duct Tape"
    #     # why the fuck is the else not picking up the variable name
    # else:  
    #     return "WD-40"


def loops_1a():
    """Make 10 stars.

    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    my_list = []

    for i in range(10):
        my_list.append("*")
    # !!! THE RETURN NEEDS TO BE ON THE SAME 
    # INDENT AS THE FOR LOOP ... FFS!
    return my_list

    


def loops_1c(number_of_items=5, symbol="#"):
    """Respond to variables.

    Using any method, return a list of number_of_items items, each one a
    string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']
    """

    symbol_list = []
    for i in range(number_of_items):
        symbol_list.append(symbol)
    
    return symbol_list


def loops_2():
    """Make a big square starfield.

    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
          ]
    """

    # up to here. Fix this !!!
    # starfield = []
    #sub_list = []
    #mid_list = []

    # for i in range(10):
    #     sub_List = []
    #     sub_List.append("*")
    #     for j in range(10):
    #         mid_list = []
    #         mid_list.append(sub_List[9])
    #         starfield.append(mid_list)
    
    # return starfield
    # nooooooooooooope 

    starfield = []

    for i in range(10):
        sub_list = []
        for j in range(10):
            sub_list.append('*')
        starfield.append(sub_list)
            
    return starfield
    # not 100% clear... draw a diagram. work it out.



    
        



def loops_3():
    """Make a rising block of numbers.

    Return this:
    [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
        ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
        ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
        ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
        ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
        ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
        ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
    ]
    remember that range(10) produces a list of numbers from 0...9
    So for every step produced by `for i in range(10):` i is a different number
    TIP: notice that this needs to to return strings of numbers,
         so call str(number) to cast.
    """

    block = []

    for i in range(10):
        inner_block = []
        for j in range(10):
            # cast the iterator to string here
            inner_block.append(str(i))
            #dont do the below... do it earlier
            #conversion = str(inner_block)
        block.append(inner_block)
    
    return block




def loops_4():
    """Make a block of numbers that rises left to right.

    Return this:
    [
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    """
    # make empty list for first loop [0...9]
    in_rise_block = []
    # make another empty list for second loop [outside of prev. loop]
    # no don't do this... see below
    # out_rise_block = []
    
    for i in range(10):
        # append to list OUTSIDE of loop - so the contents get called again
        # also... don't forget to cast contents of list to a STRING
        in_rise_block.append(str(i))
        # having the list created INSIDE the first loop seems to be the key
        out_rise_block = []
        for j in range(10):
            out_rise_block.append(in_rise_block)
        
        # naming of variables, eg "inner/ outer" can get confusing
        # "in" meaning inner container of data [list], not inner loop
        # "out" meaning outer container, single item list [of lists]

    return out_rise_block


def loops_5():
    """Make the coordinates of the block.

    Return this:
    [
      ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)'],
      ['(i1, j0)', '(i1, j1)', '(i1, j2)', '(i1, j3)', '(i1, j4)'],
      ['(i2, j0)', '(i2, j1)', '(i2, j2)', '(i2, j3)', '(i2, j4)'],
      ['(i3, j0)', '(i3, j1)', '(i3, j2)', '(i3, j3)', '(i3, j4)'],
      ['(i4, j0)', '(i4, j1)', '(i4, j2)', '(i4, j3)', '(i4, j4)'],
      ['(i5, j0)', '(i5, j1)', '(i5, j2)', '(i5, j3)', '(i5, j4)'],
      ['(i6, j0)', '(i6, j1)', '(i6, j2)', '(i6, j3)', '(i6, j4)'],
      ['(i7, j0)', '(i7, j1)', '(i7, j2)', '(i7, j3)', '(i7, j4)'],
      ['(i8, j0)', '(i8, j1)', '(i8, j2)', '(i8, j3)', '(i8, j4)'],
      ['(i9, j0)', '(i9, j1)', '(i9, j2)', '(i9, j3)', '(i9, j4)']
    ]

    TIP:
    You can construct strings either by concatinating them:
        "There are " + str(8) + " green bottles"
    or by using format:
        "There are {} green bottles".format(8)
    you'll come to see the pros and cons of each over time.
    """
    a_list = []
    
    for i in range(10):
        # 10 lists
        first_line = []
        for j in range(5):
            # using the concatenating method as to include multiple iterators
            first_line.append("(i" + str(i) + ", j" + str(j) + ")")
        a_list.append(first_line)

    return a_list


def loops_6():
    """Make a wedge of numbers.

    Return this:
    [
      ['0'],
      ['0', '1'],
      ['0', '1', '2'],
      ['0', '1', '2', '3'],
      ['0', '1', '2', '3', '4'],
      ['0', '1', '2', '3', '4', '5'],
      ['0', '1', '2', '3', '4', '5', '6'],
      ['0', '1', '2', '3', '4', '5', '6', '7'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    You don't have to use a literal number in the range function.
    You can use a variable.
    TIP: look out for the starting condition.
    """
    # i've accidentally already done this previously somewhere....

    # issue... first list = empty. Get to the bottom of this... 

    wedge = []
    
    for i in range(10):
        inner = []
        # j does not have a value for the first iteration of i ???
        # fix = add "+1" to resolve value [plus to get to the full range]
        for j in range(i + 1):
            # don't forget to cast to string
            inner.append(str(j))
        # appending list in previous indent = initial "i" loop?
        # ... sanity check    
        wedge.append(inner)
    

    return wedge
    



def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """
    # list of 5 sub-lists // each sub-list has 9 items [not 10!]
    
    # 9 - 5 - j     // gives index of start postition
    # j + 2         // 2, 3, 4, 5, 7 // fuck 
    # get some sleep. 

    # re-appraoch this.

    # fin_list = []

    # for i in range(5):
    #     first_container = []
    #     for j in range(9):
    #         click = j + 1
    #         first_container[(9-4)-click].append('*')
    #     fin_list.append(first_container)
    
    # return None

    # no trickery here...  

    # 0 + 1; 1 + 2; 2 + 3; etc

    # franz_list = []

    # five lists
    # for i in range(5):
    #     inner = []
    #     for j in range(i):
    #         # deeper = []
    #         for k in range(i + (j+1)):
    #             inner.append("*")
        
    #     franz_list.append(inner)
    
    # return franz_list

    pyramid = []

    for i in range(5):
        container = []
        for j in range(9):
            # set bounds for stars to be appended into list
            # starting below index 3, with iterator to increase
            # other bounds... if greater than + iterator
            # ffs
            if j > (3 - i) and j < (5 + i):
                container.append('*')
            else:
                container.append(' ')
        # FUCKING INDENTS
        pyramid.append(container)
    
    return pyramid
            







def little_printer(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    if some_kind_of_list is not None:
        print("\n" + exercise_name)
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print(column, end="")
                print()
        else:
            for column in some_kind_of_list:
                print(column, end="")
            print()
    else:
        print(exercise_name, "maybe you haven't got to this one yet?")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    print(is_odd(1), "is_odd odd")
    print(is_odd(4), "is_odd even")
    print(fix_it(True, True), "fix_it")
    print(fix_it(True, False), "fix_it")
    print(fix_it(False, True), "fix_it")
    print(fix_it(False, False), "fix_it")
    little_printer(loops_1a(), "loops_1a")
    little_printer(loops_1c(4, "×°×"), "loops_1c")
    little_printer(loops_2(), "loops_2")
    little_printer(loops_3(), "loops_3")
    little_printer(loops_4(), "loops_4")
    little_printer(loops_5(), "loops_5")
    little_printer(loops_6(), "loops_6")
    little_printer(loops_7(), "loops_7")
