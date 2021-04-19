#! /usr/bin/env python3

"""Thompson's construction implementation"""

# Alex Burns - G00376755

# Based on code provided by Ian McLoughlin found here: https://github.com/ianmcloughlin/graph-theory-python/blob/main/thompson.py

class State:
    """Class representation of a state and it's arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        self.label = label
        # List of outgoing arrows from the current state.
        self.arrows = arrows
        # Boolean marks the current state as or not as an accept state.
        self.accept = accept

    def followes(self):
        """Returns the set of states that are pointed to by this state that have e arrows"""
        # Include current state in returned set.
        states = {self}
        # If this state has e arrows (label is None).
        if self.label is None:
                # Loop through this state's arrows.
                for state in self.arrows:
                    # Incoporate that state's e arrows in the set states.
                    states = (states | state.followes())
        # Return the set of states.
        return states

class NFA:
    """Class representation of of a non-deterministic finite automaton."""
    def __init__(self, start, end):
        # Start state of the current NFA.
        self.start = start
        # End state of the current NFA.
        self.end = end

    def match(self, s):
        """Return true iff this NFA(instance) matches the string s."""
        # Set of previous states that we are still in.
        previous = self.start.followes()
        # Loop through the string s a character at a time.
        for c in s:
            # Start with an empty set of current states.
            current = set()
            # Loop through the states in set previous. 
            for state in previous:
                # If there is a c arrow from the current state.
                if state.label == c:
                    # Add followes for next state.
                    current = (current | state.arrows[0].followes())
            # Replace the set previous with the set current.
            previous = current
            
        # If the NFAs end state is in the set previous the string has matched, else it has not matched.
        return (self.end in previous)

def re_to_nfa(postfix):
    # NFA stack used in thompson's construction algorithm.
    stack = []

    # Looping through the postfix r.e. from left to right.
    for c in postfix:
        # Concatenation
        # If current character is the special character for concatenation '.'.
        if c == '.':
            # Pop off and store NFA at the top of NFA stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop off and store next NFA at the top of NFA stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Set accept state of nfa1 to non-accept.
            nfa1.end.accept = False
            # Point the end state of nfa1 at the start state of nfa2.
            nfa1.end.arrows.append(nfa2.start)
            # Create new NFA with nfa1's start state as the start state and nfa2's end state as the ned state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push new NFA to NFA stack.
            stack.append(nfa)

        # OR
        # Else if current character is the special character for or '|'.
        elif c == '|':
            # Pop off and store NFA at the top of NFA stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop off and store next NFA at the top of NFA stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create a start state and end state.
            start = State(None, [], False)
            end = State(None, [], True)
            # Point arrows from newly made start state to start states nfa1 and nfa2.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Set nfa1 and nfa2's end states to non-accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point arrows from end states of nfa1 and nfa2 at the newly made end state.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            #  Create new NFA with previously created start state as it's start state and previously created end state as it's end state.
            nfa = NFA(start, end)
            # Push new NFA to NFA stack.
            stack.append(nfa)

        # Kleene Star
        # Else if current chracter is the special character for kleene start '*'
        elif c == '*':
            # Pop off and store NFA at the top of NFA stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create a start state and end state.
            start = State(None, [], False)
            end = State(None, [], True)
            # Point arrow from newly made start state at the start state of nfa1.
            start.arrows.append(nfa1.start)
            # Point arrow from newly made start state at newly made end state.
            start.arrows.append(end)
            # Set nfa1's end state to non-accept.
            nfa1.end.accept = False
            # Point arrow from nfa1's end state to the newly made end state.
            nfa1.end.arrows.append(end)
            # Point arrow from nfa1's end state to nfa1's start state.
            nfa1.end.arrows.append(nfa1.start)
            #  Create new NFA with previously created start state as it's start state and previously created end state as it's end state.
            nfa = NFA(start, end)
            # Push new NFA to NFA stack.
            stack.append(nfa)

        # Non-special character   
        # Else current character is a non-special character.
        else:
            # Create an end state.
            end = State(None, [], True)
            # Create a start state with the label containing the non-special character.
            start = State(c, [], False)
            # Point arrow from newly made start state to newly made end state.
            start.arrows.append(end)
            #  Create new NFA with previously created start state as it's start state and previously created end state as it's end state.
            nfa = NFA(start, end)
            # Push new NFA to NFA stack.
            stack.append(nfa)

    # If there is any more or less than one NFA on the NFA stack after main loop.
    if len(stack) != 1:
        # Something went wrong.
        return None
    # Else there is only one NFA on the NFA stack after main loop.
    else:
        # Return the final fully constructed NFA.
        return stack[0]
