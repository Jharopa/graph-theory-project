#! /usr/bin/env python3

"""Project tests"""

# My imports.
from shunting import shunt

def test_shunt():
    infixs   = ['', 'a', 'a.a', 'a.b', 'a|c', 'a*', 'x*.y.z', 'a.(b.b)*.a', '1.(0.0)*.1', '1.(0.1)*.(1|0)']
    expected = ['', 'a', 'aa.', 'ab.', 'ac|', 'a*', 'x*y.z.','abb.*.a.', '100.*.1.', '101.*.10|.']

    print("Tests for Shunting Yard algorithm function shunt() found in shunting.py\n")

    for i in range(len(infixs)):
        postfix = shunt(infixs[i])
        passed = (postfix == expected[i])

        print(f"Test {(i + 1)}")
        print(f"Infix: {infixs[i]}")
        print(f"Expected postfix: {expected[i]}")
        print(f"Shunt postfix: {postfix}")
        print(f"Passed: {passed}\n")
