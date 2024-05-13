from Movie_utilities import get_by_year
movies_list = [
    "The Shawshank Redemption|1994",
    "Pulp Fiction|1994",
    "The Godfather|1972",
    "The Matrix|1999",
    "The Lord of the Rings: The Return of the King|2003",
    "The Godfather: Part II|1974"
]
selected_year = 1994
ymovies = get_by_year(movies_list, selected_year)
print(ymovies)