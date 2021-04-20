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
python scripts.py "(<.c.a.l.o.r.i.e.s.>)|(<./.c.a.l.o.r.i.e.s.>)" example.txt
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

Resources used to understand and implement Thompson's Construction:
- Lecture by Ian McLoughlin found [here](https://web.microsoftstream.com/video/9ddadf79-1e30-46d9-b1b5-63070e6d7a10)
- Youtube video going through a working example found [here](https://www.youtube.com/watch?v=Jd71l0cHZL0)
- Shunting Yard Wikipedia page found [here](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

### Thompson's Construction Algorithm
Thompson's Construction is an algorithm that, as mentioned before, takes a regular expression in postfix notation as its input then, using that regular expression and a stack data structure, builds and outputs a Non-Deterministic Finite Automaton(NFA) representing said regular expression. 

A NFA is an atomaton made up of several states with unidirectional transitions between said states that are marked by one of several input symbols. All NFAs contain two special states a starting state, and a accepting state. NFAs in Thompson's Contruction also contain a special input symbol `ε` denoting the empty string character.

The algorithm builds the overall NFA from the postfix regular expression in a recursive manner, creating smaller NFAs when a operand character is read in from the regular expression. An example of a NFA for the character `a` would be structured like this:

![a NFA](https://github.com/Jharopa/graph-theory-project/blob/main/readme_media/aNFA.PNG)

(Note. The state with the arrow coming in from nowhere is the start state and the double circle is the accept state) 

This NFA is then added to a stack and the process is repeated until an operator is read. When an operator is read the last one or two operand NFA(s) (amount dependant on the operator read) created and pushed to the stack previously, are popped off the stack and used to created a larger NFA which is then pushed back onto the stack. An example of a NFA for the expression `ab|` would be structured like this:

![a OR b](https://github.com/Jharopa/graph-theory-project/blob/main/readme_media/aorb.png)

(Note. The new location of the start and accept state for the greater NFA.)

The previous steps are then repeated until the entire regular expression has been read through and the full NFA has been built and assembled.

This program allows for the following regular expression operators:

| Operation | Symbol | Resulting NFA |
| --- | --- | --- |
| Concatenation | . | ![Concatenation](https://github.com/Jharopa/Markdown/blob/main/readme_media/concat.png) |
| Or | \| | ![Or](https://github.com/Jharopa/Markdown/blob/main/readme_media/or.png) |
| Zero or Many | * | ![Kleene](https://github.com/Jharopa/Markdown/blob/main/readme_media/kleene.png) |

The implemention of Thompson's Contruction algorithm used in this program can be found in `thompson.py` and is made up of the python classes `State` and `NFA` along with the function `re_to_nfa`.

Resources used to understand and implement Thompson's Construction:
- Medium article by Gregory Cernera found [here](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)
- Blog post by Russ Cox found [here](https://swtch.com/~rsc/regexp/regexp1.html)
- Lectures by Ian McLoughlin found [here](https://web.microsoftstream.com/video/d6d9a2d8-b23e-4abf-b1b7-af3a2d44b82f), [here](https://web.microsoftstream.com/video/634e1883-ad11-447f-971a-cb7965355c13?referrer=https:%2F%2Flearnonline.gmit.ie%2F) and [here](https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32)
- Thompson's Construction Wikipedia page found [here](https://en.wikipedia.org/wiki/Thompson%27s_construction)


### String Matching Algorithm
The string matching algorithm, used to match a given string against the NFA created from a regular expression, is implemented again in `thompson.py`, found in the `NFA` classes member function `match`. This `match` function subsequently uses the recursive helper function `followes` which is a member function of the class `State`.

The algorithm takes a string as its input and tests it against the previously constructed NFA. This is done by begining in the start state of the NFA and iterating over the input string's characters then following a transition to the next state if the transitions symbol matches the current string character. 

It is important to highlight that the input string can have multiple instances of itself in multiple states at any given time(Hence the 'Non-Deterministic'), with the `ε` symbol transitions being followed as soon as the state with these transitions have been entered. An instance of the string in a given state will no longer be followed if there is no way for the current string to transition to another state

The input string's characters are completly run through and the string is siad to have 'matched' the NFA, and the regular expression it has been constructed from, if when all string characters have been iterated over at least one instance of the string is in the NFA's accept state. In this programs implementation the function `match` will return `True` if this condition is met and `False` otherwise.

Resources used to understand and implement String Matching Algorithm:
- Lectures by Ian McLoughlin found [here](https://web.microsoftstream.com/video/8fe195b7-f7c3-4265-86bc-7ff2c367eee9), [here](https://web.microsoftstream.com/video/0f3d8f6f-68c9-42d0-9449-b7f868888efe) and [here](https://web.microsoftstream.com/video/59770e5a-2fed-4575-a4eb-0fd691b77d54)

### File Searching Algorithm
A comparatively simple algorithm, takes a regular expression and file name string as input, builds a NFA from the regular expression, then opens the file with the name provided and reads in the file line by line. Each line is passed to the NFA's matching function and then displayed to the CLI if matching function returns `True`, otherwise it is not displayed.

## Awnsers
