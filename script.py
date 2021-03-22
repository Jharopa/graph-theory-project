#! /usr/bin/env python3

# Alex Burns

# Based on code from the site Real Python found here: https://realpython.com/command-line-interfaces-python-argparse/

# Python library imports.
import argparse

from test import test_shunt

# Main.
def main():
    # AgumentParser for program.
    parser = argparse.ArgumentParser(description="regular expression text file searcher")

    # Positional arguments.
    parser.add_argument('regex', nargs='?', 
                        help='the regular experssion you would like to search for, must be used with path (format: script.py <regex> <path>)')
    parser.add_argument('path', nargs='?', 
                        help='the path to the file you would like to search (format: absolute path of file)')

    # Optional arguments.
    parser.add_argument('-t', '--test',
                        help='runs pre-made tests created for the program (tests found in test.py)',
                        action='store_true')

    # Get aguments from parser.
    args = parser.parse_args()
    
    # If the regex and file path are passed as aguments.
    if args.regex and args.path:
        print(f'{args.regex}, {args.path}')
    # Else if --test or -t is passed as optional argument.
    elif args.test:
        test_shunt()
    # Else if arguments are not one of the accepted formats (script.py <regex> <path> or script.py --test/-t)
    else:
        print('Please refer to documentation or --help/-h for valid program arguments')

if __name__ == '__main__':
    main()
