"""
------------------------------------------------------------------------
Assignment 1, Task 4
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-04-07'
------------------------------------------------------------------------
"""

from functions import file_analyze
with open("t02.txt", "r", encoding="utf-8") as fh_1:
    # Call file_analyze function and pass the open file handle fh_1
    upp, low, dig, whi, rem = file_analyze(fh_1)
    # Now you can use the results as needed, maybe print them or process them further
    print(f"Uppercase: {upp}, Lowercase: {low}, Digits: {dig}, Whitespace: {whi}, Others: {rem}")