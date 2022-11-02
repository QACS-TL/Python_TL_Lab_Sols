#! /bin/python
# Name:        search.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Download the top 250 movies chosen by IMDb users.
"""
    Download and display online movie information.
"""
import sys
import imdb
import re

def search_movie(pattern):
    """ Search for a Regex pattern in the top 250 movies """
    ia = imdb.IMDb()
    count = 0
    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        m = re.search(pattern, str(movie), re.IGNORECASE)
        if m:
            print(f"{rank:>4}: {movie}")
            count += 1
    print(f"Matched {count} lines")
    return None

def main():
    """ The Main Program """
    search_movie(r"^the") # 50 lines.
    search_movie(r"[0-9]")  # 11 lines.
    search_movie(r"[aeiou]{3}")  # 5 lines.
    search_movie(r"^(.).*\1$") # 15 lines.
    search_movie(r"^[^a-zA-Z]+$")  # 1 line.
    search_movie(r"monty")  # 1 lines.
    search_movie(r"\s+(\w+)\s+.*\1\s+")  # 8 lines.
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)