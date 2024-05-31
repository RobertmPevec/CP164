"""
------------------------------------------------------------------------
Lab 3, Task 2
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-25'
------------------------------------------------------------------------
"""
from Stack_array import Stack

# Initialize the stack and test data
source_stack = Stack()
test_data = [8, 14, 12, 9, 8, 7, 5, 5, 8, 12, 8, 7, 9, 14]

for item in test_data:
    source_stack.push(item)


def print_stack(stack):
    return list(stack._values)

print(print_stack(source_stack))

target1, target2 = source_stack.split_alt()

print(print_stack(target1))
print(print_stack(target2))