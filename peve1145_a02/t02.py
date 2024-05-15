"""
------------------------------------------------------------------------
Assignment 2, Task 2
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-15'
------------------------------------------------------------------------
"""

from Movie_utilities import get_by_rating
movies_list = [
    "Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8",
    "Dark City|1998|Alex Proyas|7.8|0",
    "Zulu|1964|Cy Endfield|7.8|9",
    "I Am Legend|2007|Francis Lawrence|7.1|0,6",
    "Omega Man, The|1971|Boris Sagal|6.6|0,6",
    "Last Man On Earth, The|1964|Ubaldo Ragona|6.9|0",
    "Alphaville|1965|Jean-Luc Godard|7.1|0,4",
    "Stardust|2007|Matthew Vaughn|7.7|1,4",
    "Juno|2007|Jason Reitman|7.7|3,4",
    "Darjeeling Limited, The|2007|Wes Anderson|7.1|4",
    "Broken Flowers|2005|Jim Jarmusch|7.2|3,4",
    "Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6",
    "Horror of Dracula|1958|Terence Fisher|7.4|8",
    "Jason and the Argonauts|1963|Don Chaffey|7.4|1,6",
    "Wrong Box, The|1966|Bryan Forbes|7.0|4",
    "Finding Dory|2016|Andrew Stanton, Angus MacLane|7.5|4",
    "Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8",
    "Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8",
    "Z|1969|Costa-Gavras|8.2|2",
    "Wonder Woman|2017|Patty Jenkins|8.1|1,6",
    "Zulu|2013|Jerome Salle|6.7|2"
]
selected_rating = 8
rmovies = get_by_rating(movies_list, selected_rating)
print(rmovies)
