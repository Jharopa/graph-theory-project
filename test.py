#! /usr/bin/env python3

"""Project tests"""

# My imports.
from shunting import shunt
import 

def test_shunt():
    """Tests the regular expression infix to postfix conversion implemented in the shunt()"""
    # List of regular expressions in infix notation.
    infixs   = ['', 'a', 'a.a', 'a.b', 'a|c', 'a*', 'x*.y.z', 'a.(b.b)*.a', '1.(0.0)*.1', '1.(0.1)*.(1|0)']
    # List of regular expressions in postfix notation.
    expected = ['', 'a', 'aa.', 'ab.', 'ac|', 'a*', 'x*y.z.','abb.*.a.', '100.*.1.', '101.*.10|.']

    print("Tests for Shunting Yard algorithm function shunt() found in shunting.py\n")

    # For i from 0 to the lenght of the infixs list.
    for i in range(len(infixs)):
        # Set postfix to the result of shunt() when passed infixs[i]
        postfix = shunt(infixs[i])
        # Set passed to True if postfix is equal to expected[i], else set it to False.
        passed = (postfix == expected[i])

        # Print result.
        print(f"Test {(i + 1)}")
        print(f"Infix: {infixs[i]}")
        print(f"Expected postfix: {expected[i]}")
        print(f"Shunt postfix: {postfix}")
        print(f"Passed: {passed}\n")

