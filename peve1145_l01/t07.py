"""
------------------------------------------------------------------------
Lab 1, Task 7
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-11'
------------------------------------------------------------------------
"""

from Movie_utilities import read_movies
with open('movies.txt', 'r') as file:
    movies = read_movies(file)
print(movies)