#! /usr/bin/env python3

"""Regular expression file checker"""

# Alex Burns - G00376755

# Based on code from the site Real Python found here: https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file

# My imports.
from shunting import shunt
import thompson

def check_file(regex, file):
    """Checks each line of text in file against NFA produce using regular expression provided and prints the line if it matches."""
    # Get regular expression in postfix notation.
    postfix = shunt(regex)
    # Created NFA using postfix regular expression.
    nfa = thompson.re_to_nfa(postfix)

    # Open the file.
    with open(file, 'r') as reader:
        # Read in the first line.
        line = reader.readline()
        # While the line read in is not the EOF character.
        while line != '':
            # Remove new line character from line.
            line = line.rstrip('\n')
            if nfa.match(line) == True:
               print(line)
            # Read in the next line.
            line = reader.readline()