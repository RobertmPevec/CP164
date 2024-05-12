"""
------------------------------------------------------------------------
Lab 1, Task 2
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-11'
------------------------------------------------------------------------
"""

from Movie import Movie
movie_instance = Movie("Zulu", 2013, "Jerome Salle", 6.7, [2, 3, 6])
genres_string = movie_instance.genres_list_string()
print(genres_string)
