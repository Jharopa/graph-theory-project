#! /usr/bin/env python3

"""Shunting Yard for Regular Expressions"""

# Alex Burns

# Based on code provided by Ian McLoughlin found here: https://github.com/ianmcloughlin/graph-theory-python/blob/main/shunting-re.py
# Original code based on shunting yard psudocode found here: https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expression to postfix expression"""

    # Output stack.
    postfix = ""
    # Shunting yard stack.
    stack = ""
    #Operator precedence(* > . > |).
    prec = {'*': 100, '.': 90, '|': 80}

    # Loop through the function input a character at a time.
    for c in infix:
        # If c is an operator.
        if c in {'*', '.', '|'}:
            # Check what is on the shunting yard stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator to top of output stack.
                postfix = postfix + stack[-1]
                # Remove operator from shunting yard stack.
                stack = stack[:-1]
            
            #Push c to shunting yard stack.
            stack = stack + c

        # Else if c is a left parenthesis.
        elif c == '(':
            # Push c to shunting yard stack.
            stack = stack + c

        # Else if c is right parenthesis.
        elif c == ')':
            # While the last thing on the shunting yard stack is not a left parenthesis.
            while stack[-1] != '(':
                #Append operator at top of output stack.
                postfix = postfix + stack[-1]
                # Remove operator from shunting yard stack.
                stack = stack[:-1]

            # Finally remove left parenthesis from shunting yard stack.
            stack = stack[:-1]
        # Else c is a non-special character.
        else:
            # Push c to the output stack.
            postfix = postfix + c

    # While shunting yard stack is not empty.
    while len(stack) != 0:
        #Append operator at top of output stack.
        postfix = postfix + stack[-1]
        # Remove operator from shunting yard stack.
        stack = stack[:-1]

    return postfix
