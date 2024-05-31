"""
------------------------------------------------------------------------
Lab 2, Task 5
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-18'
------------------------------------------------------------------------
"""

from utilities import stack_test
with open('movies.txt', 'r') as file:
    movies = file.readlines()
stack_test(movies)
