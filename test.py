#! /usr/bin/env python3

"""Project tests"""

# Alex Burns - G00376755

# Function test_nfa based on code provided by Ian McLoughlin found here: https://github.com/ianmcloughlin/graph-theory-python/blob/main/reg.py

# My imports.
from checkfile import check_file
from shunting import shunt
import thompson

def test_shunt():
    """Tests the regular expression infix to postfix conversion implemented in the shunt()"""
    # List of regular expressions in infix notation.
    infixs   = ['', 'a', 'a.a', 'a.b', 'a|c', 'a*', 'a?', 'a+','x*.y.z', 'a.(b.b)+.a', '1.(0.0)?.1', '1.(0.1)*.(1|0)']
    # List of regular expressions in postfix notation.
    expected = ['', 'a', 'aa.', 'ab.', 'ac|', 'a*', 'a?', 'a+','x*y.z.','abb.+.a.', '100.?.1.', '101.*.10|.']

    print("Tests for Shunting Yard algorithm function shunt() found in shunting.py\n")

    # For i from 0 to the lenght of the infixs list.
    for i in range(len(infixs)):
        # Set postfix to the result of shunt() when passed infixs[i]
        postfix = shunt(infixs[i])
        # Set passed to True if postfix is equal to expected[i], else set it to False.
        passed = (postfix == expected[i])

        # Print result.
        print(f"Test                {(i + 1)}")
        print(f"Infix:              {infixs[i]}")
        print(f"Expected postfix:   {expected[i]}")
        print(f"Shunt postfix:      {postfix}")
        print(f"Passed:             {passed}\n")

def test_nfa():
    """Tests NFA creation and matching functionality found in thompson.py using converted infix regular expressions produced by shunt()"""
    # List of lists containing a several infix regular expressions and the strings it is teststing.
    tests = [ 
        ["(a.b|b*)", ["ab", "b", "bb", "a", "bab"]],
        ["a.(b.b)*.a", ["aa", "abba", "aba", "abbbba"]],
        ["1.(0.0)*.1", ["11", "100001", "11001", "111"]],
        ["1.0?.1", ["10", "11", "101", "1001"]],
        ["a.b+.a", ["ab", "aa", "aba", "abbba"]],
    ]

    # Counter for tests.
    testcount = 1

    print("Tests for Thompson's construction algorithm and matching functionality found in thompson.py\n")

    # For each test in tests list.
    for test in tests:
        # Get infix regular expression from list.
        infix = test[0]
        # Find postfix notation of infix regular expression.
        postfix = shunt(infix)
        # Create NFA using postfix regular expression.
        nfa = thompson.re_to_nfa(postfix)
        # Counter for strings.
        stringcount = 1
        
        # Print test number and regular expression.
        print(f"Test:               {testcount}")
        print(f"Regex:              {infix}\n")

        for s in test[1]:
            # Check if the string matches the generated NFA.
            match = nfa.match(s)

            # Print the string and if it has matched.
            print(f"String {stringcount}:           {s}")
            print(f"Matched             {match}\n")

            # Increment string counter.
            stringcount = stringcount + 1

        # Increment test counter.
        testcount = testcount + 1

def test_searching():
    # List of regular expressions to test.
    tests = ["<.f.o.o.d.>", "<./.f.o.o.d.>", "(<.c.a.l.o.r.i.e.s.>)|(<./.c.a.l.o.r.i.e.s.>)"]
    # Counter for tests.
    testcount = 1

    print("Tests for file searching functionality found in checkfile.py\n")

    # For each test in tests list.
    for test in tests:
        # Print test number and regular expression.
        print(f"Test:               {testcount}")
        print(f"Regex:              {test}")
        print("Lines: ")

        # Call check files function passing it current regex and name of test file.
        check_file(test, "example.txt")

        # Used to create newline for formatting purposes.
        print()

        # Increment test counter.
        testcount = testcount + 1

    
