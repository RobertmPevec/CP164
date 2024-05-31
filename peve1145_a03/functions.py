"""
------------------------------------------------------------------------
Assignment 1, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""
from Stack_array import *
from enum import Enum


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    while source:
        target1.push(source.pop())
        if source:
            target2.push(source.pop())
    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp_stack = Stack()
    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())
    return None


OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    tokens = string.split()

    for token in tokens:
        if token.isdigit():
            stack.push(float(token))
        elif token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                stack.push(left / right)

    answer = stack.pop()
    return answer


from Stack_array import Stack

def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to an operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    values_out = []
    input_index = 0
    valid = True

    for operation in opstring:
        if not valid:
            break
        if operation == 'S':
            if input_index < len(values_in):
                stack.push(values_in[input_index])
                input_index += 1
            else:
                valid = False  # Invalid operation: no more items to push
        elif operation == 'X':
            if not stack.is_empty():
                values_out.append(stack.pop())
            else:
                valid = False  # Invalid operation: nothing to pop
        else:
            valid = False  # Invalid operation: unexpected character

    # Ensure all input values are processed and the stack is empty
    if input_index != len(values_in) or not stack.is_empty():
        valid = False

    if not valid:
        values_out = None

    return values_out


MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, f"cannot use '{m}' as the mirror character"

    result = MIRRORED.NOT_MIRRORED

    parts = string.split(m)
    if len(parts) == 2:
        left, right = parts

        stack = Stack()

        invalid_char = False
        for char in left:
            if char not in valid_chars:
                invalid_char = True
                result = MIRRORED.INVALID_CHAR
            else:
                stack.push(char)

        if not invalid_char:
            mismatched = False
            for char in right:
                if char not in valid_chars:
                    invalid_char = True
                    result = MIRRORED.INVALID_CHAR
                    break
                if stack.is_empty() or stack.pop() != char:
                    mismatched = True
                    result = MIRRORED.MISMATCHED

            if not invalid_char and not mismatched:
                if not stack.is_empty():
                    result = MIRRORED.TOO_MANY_LEFT
                else:
                    result = MIRRORED.IS_MIRRORED

    return result
