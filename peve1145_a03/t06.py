"""
------------------------------------------------------------------------
Lab 3, Task 6x`
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""

from functions import reroute

test_cases = [
    ("SSXSSXXX", [1, 2, 3, 4]),
    ("SSXXSXSX", [1, 2, 3, 4]),
    ("SSSSXXXX", [1, 2, 3, 4]),
    ("SXSXSXSX", [1, 2, 3, 4]),
    ("SXSSXSXS", [1, 2, 3, 4]),
    ("SXX", [1, 2, 3, 4]),
    ("SSXSSXX", [1, 2, 3, 4]),
]


def test_reroute(test_cases):
    for opstring, values_in in test_cases:
        result = reroute(opstring, values_in)
        print(f"opstring: {opstring}, values_in: {values_in} => result: {result}")


test_reroute(test_cases)
