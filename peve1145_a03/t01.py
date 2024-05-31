"""
------------------------------------------------------------------------
Lab 3, Task 1
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""
from functions import stack_split_alt
test_data = [8, 14, 12, 9, 8, 7, 5, 5, 8, 12, 8, 7, 9, 14]
target1, target2 = stack_split_alt(test_data)


def print_stack(stack):
    return list(stack._values)


print(print_stack(target1))
print(print_stack(target2))
