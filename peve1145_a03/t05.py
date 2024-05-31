"""
------------------------------------------------------------------------
Lab 3, Task 5
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""
from functions import postfix

expressions = [
    "12 5 -",
    "4 5 + 12 * 2 3 * -",
    "3 4 + 2 * 7 /",
    "5 1 2 + 4 * + 3 -"
]


def test_postfix(expressions):
    for expr in expressions:
        result = postfix(expr)
        print(result)


test_postfix(expressions)
