"""
------------------------------------------------------------------------
Lab 3, Task 4
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""

from Stack_array import Stack

source_stack = Stack()
test_data = [8, 14, 12, 9, 8, 7, 5, 5, 8, 12, 8, 7, 9, 14]

for item in test_data:
    source_stack.push(item)


def print_stack(stack):
    return list(stack._values)

print(print_stack(source_stack))
source_stack.reverse()
print(print_stack(source_stack))
