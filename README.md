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
python scripts.py (o.o)|(I.n) lorem.txt
```

### Running the tests
To run the premade tests that are included with the program you can use the command:
```bash
python scripts.py --test
```
This will produce the results of the tests in the CLI, these tests cover the three main parts of of this program, the Shunting yard algorithm implementation, the Thompson's construction algorithm implementation, and the file searching functionality.

## Algorithms

## Awnsers
