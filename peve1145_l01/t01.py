"""
------------------------------------------------------------------------
Lab 1, Task 1
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-11'
------------------------------------------------------------------------
"""

from Movie import Movie
movie_instance = Movie("Zulu", 2013, "Jerome Salle", 6.7, [2])
genre_string = movie_instance.genres_string()
print(genre_string)
