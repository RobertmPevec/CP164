"""
------------------------------------------------------------------------
Lab 2, Task 1
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-18'
------------------------------------------------------------------------
"""

from Stack_array import Stack
s = Stack()
b = s.is_empty()
print(b)
s.push(10)
print(s._values)
value = s.pop()
print(s._values)
s.push(10)
value = s.peek()
print()
