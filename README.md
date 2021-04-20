# Project: Graph Theory 2021
Student name: Alex Burns <br />
Student ID: G00375766

## What is this repo?
This repository and its readme is a project created for 3rd Year Graph Theory 2021 at GMIT. For this project the following problem statment, presented by [Ian McLoughlin](https://github.com/ianmcloughlin), was given:

> In this project you must write a program in the Python 3 programming language to search a text file using a regular expression. Your program must take a regular expression and the name or path of the file as command line arguments and output the lines of the file matching the regular expression. You have a lot of freedom in how you interpret the term regular expression, as will be discussed in class. It will likely be easier to limit yourself to regular languages. <br /> <br />
The program must be coded from scratch. You cannot use any external libraries other than what is included in Python, and you cannot use the `re` package included there. Any extra features added to your script must be your own work. You must also include tests which run upon `python script.py --test` being called, as will be described in lectures. The tests should ensure that your regular expression engine works on a sensible example list of inputs.

Therefore in this reposistory you will the find files for a python program that builds a regular expression engine from scratch along with the functionality needed to use said engine to search a text file and return the lines that contain matches to a user defined regular expression. There will also be python file containing a set of tests that can be used to test the different parts of the regular expression engine and the file searching functionality.

Below this description you will find several sections contianing the following information:
- Instructions - Setting up your enviroment, running the program, and running the tests.
- Algorithms - Explanation of the algorithms employed to create this program.
- Answers - The answers to three questions present in the brief for this project:

  > - What is a regular expression?
  > - How do regular expressions differ across implementations?
  > - Can all formal languages be encoded as regular expressions?

## Instructions

### Enviroment Setup
To setup the enviroment to run this program you must first have both [python](https://www.python.org/downloads/) and [GIT](https://git-scm.com/downloads) installed. Once both of these have been acquired and installed, using a your systems CLI navigate to where you would like to install this program and clone this repository using the command:
```bash
git clone https://github.com/Jharopa/graph-theory-project.git
```

### Running the program
Before running the program you must provide the text file you would like to search by placing said text file into the `graph-theory-project` directory alongside `script.py`. Once the file you would like to search is within the directory, again using your systems CLI, navigate into the `graph-theory-project` directory.

The program can then be run using the command `python script.py <regex> <file>` where the `<regex>` is the regular expression you would like to search against and `<file>` is the name of the file you would like to search. Included in this repo is a text file called `lorem.txt` used as part of the tests, using this command to search this file would look like this:
```bash
python scripts.py "(a.b|b*)" example.txt
```
The regular expression should be enclosed in quotes when the `|` character is used as it is an operator used by many system CLI's and the qoutes indicate to the CLI that the `|` should be read as part of the regular expression string.

### Running the tests
To run the premade tests that are included with the program you can use the command:
```bash
python scripts.py --test
```
This will produce the results of the tests in the CLI, these tests cover the three main parts of of this program, the Shunting yard algorithm implementation, the Thompson's construction algorithm implementation, and the file searching functionality.

## Algorithms

### Shunting Yard Algorithm
An implementation of the [Shunting Yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) is employed in this program, found in `shunting.py`. This particular implementation accepts a user defined regular expression in infix notation as input, and outputs the same regular expression in postfix notation, an example being the infix `a.b|c` would be converted to `ab.c|`. The conversion from infix to postfix is facilitated through the use of several stack data structures with the operators and operands of an expression being moved between stacks in a specific order based on a defined order of precedence.

An excellent illustration of this process can be found [here](https://upload.wikimedia.org/wikipedia/commons/2/24/Shunting_yard.svg) (Note. this illustration uses the operators `+ - x`, however the algorithm can also be applied to regular expressions and it's operators). This algorithm is neccessary for this program as the next algorithm, Thompson's Construction, requires regular expression in postfix notation as its input.

### Thompson's Construction Algorithm
Thompson's Construction is an algorithm that, as mentioned before, takes a regular expression in postfix notation as its input then, using that regular expressionand a stack data structure, builds and outputs a Non-Deterministic Finite Automaton(NFA) representing said regular expression. 

A string can then be checked against the resulting NFA by begining in the NFAs start state and iterating through each character in the string, traversing between the NFAs states depending on the current character. The string can then be said to have "matched" the NFA, and the regular expression it was built from, if the string is in the NFAs accept state by the time every character in the string has been iterated through.

The algorithm builds the overall NFA from the postfix regular expression in a recursive manner, creating smaller NFAs when a operand character is read in from the regular expression. An example of a NFA for the character `a` would be structured like this:

<img src="https://github.com/Jharopa/graph-theory-project/blob/main/readme_media/aNFA.PNG" width="450" height="150">![]()

(Note. The state with the arrow coming in from nowhere is the start state and the double circle is the accept state) 

This NFA is then added to a stack and the process is repeated until an operator is read. When an operator is read the last one or two operand NFA(s) (amount dependant on the operator read) created and pushed to the stack previously, are popped off the stack and used to created a larger NFA which is then pushed back onto the stack. An example of a NFA for the expression `ab|` would be structured like this:

<img src="https://github.com/Jharopa/graph-theory-project/blob/main/readme_media/aorb.png" width="600" height="250">

(Note. 1.) The new location of the start and accept state for the greater NFA. 2.) The `ε` character, this represents the empty string character, more on this later)

The previous steps are then repeated until the entire regular expression has been read through and the full NFA has been built and assembled.

## Awnsers
