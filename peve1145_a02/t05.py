"""
------------------------------------------------------------------------
Assignment 2, Task 5
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-15'
------------------------------------------------------------------------
"""

from Movie_utilities import genre_counts
with open('movies.txt', 'r') as file:
    movies = genre_counts(file)
print(movies)
