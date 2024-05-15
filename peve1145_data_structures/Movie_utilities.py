"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Robert Pevec
ID:      169081145
Email:   peve1145@mylaurier.ca
Section: CP164 B
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    parts = line.split("|")
    title = parts[0]
    year = int(parts[1])
    director = parts[2]
    rating = float(parts[3])
    genres = list(map(int, parts[4].split(',')))
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """
    movies = ""
    for line in fv:
        if movies:
            movies += "\n"
        movies += line
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    print(Movie.genres_menu())
    has_selected_at_least_one_genre = False
    genre_numbers = []
    while True:
        answer_key = input("Enter a genre number (ENTER to quit):")
        if answer_key == "":
            if has_selected_at_least_one_genre:
                break
            else:
                print("Error: must have at least one genre")
        elif answer_key.isdigit():
            genre_number = int(answer_key)
            if genre_number in genre_numbers:
                print("Error: genre already chosen")
            elif genre_number < 0:
                print("Error: not a positive number")
            elif genre_number > 10:
                print("Error: input must be <= 10")
            elif 0 <= genre_number <= 10:
                genre_numbers.append(genre_number)
                has_selected_at_least_one_genre = True
        else:
            print("Error: not a positive number")
    return sorted(genre_numbers)


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    for movie in movies:
        parts = movie.split("|")
        movie_year = int(parts[1])
        if movie_year == year:
            title = parts[0]
            ymovies.append(title)
    return ymovies

def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies = []
    for r in movies:
        parts = r.split("|")
        movie_rating = float(parts[3])
        if movie_rating >= rating:
            title = parts[0]
            rmovies.append(title)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    for g in movies:
        parts = g.split("|")
        genres = list(map(int, parts[4].split(',')))
        for n in genres:
            if n == genre:
                title = parts[0]
                gmovies.append(title)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    genres_set = set(genres)
    for m in movies:
        parts = m.split("|")
        movie_genres = list(map(int, parts[-1].split(',')))
        genres_set_compare = set(movie_genres)
        if genres_set == genres_set_compare:
            gmovies.append(parts[0])
    return gmovies

def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    count = []
    genres = Movie.GENRES
    for index in range(len(genres)):
        count.append(index - index)
    for m in movies:
        parts = m.split("|")
        if len(parts) > 4:
            movie_genres = list(map(int, parts[4].split(',')))
            for n in movie_genres:
                count[n] += 1
    return count
