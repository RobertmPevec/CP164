"""
------------------------------------------------------------------------
Lab 3, Task 7
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""
from functions import is_mirror_stack, MIRRORED

# Test cases
test_cases = [
    ("cmc", "abc", "m", MIRRORED.IS_MIRRORED),
    ("zzxzuzxzz", "xyz", "u", MIRRORED.IS_MIRRORED),
    ("cmc", "ab", "m", MIRRORED.INVALID_CHAR),
    ("zzxzxzxzz", "xyz", "u", MIRRORED.NOT_MIRRORED),
    ("zzxzuzx", "xyz", "u", MIRRORED.TOO_MANY_LEFT),
    ("abcd", "abcd", "x", MIRRORED.NOT_MIRRORED),
    ("bbbaaa", "ab", "c", MIRRORED.MISMATCHED)
]

def test_is_mirror_stack(test_cases):
    for string, valid_chars, pivot, expected in test_cases:
        result = is_mirror_stack(string, valid_chars, pivot)
        print(result.value)

test_is_mirror_stack(test_cases)