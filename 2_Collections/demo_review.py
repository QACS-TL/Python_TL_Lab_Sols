#! /bin/python
# Name:        demo_review.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will review the topics covered in
# the QA 2.0 Digital session including objects, string handling,
# file interaction, flow control, simple exception handling.
"""
    This program reads and displays a list of movies from a local
    text file containing the top 250 movies (chosen by IMDb users).
"""

menu = """
    Top Movies
    ----------
    1. Display top 250 movies.
    2. Choose Top N movies.
    3. Choose Range of movies.
    4. Choose Random movie.
"""

import random
import sys
import os

if sys.platform == "win32":
    file = r"C:\labs\movies.txt"
else:
    file = os.environ['HOME'] + r"/labs/movies.txt"

def get_movies(file):
    """ Read and return list of movies from given text file """
    movies = []
    try:
        fh_in = open(file, mode="rt")
    except:
        print("Cannot open", file)
        return None

    # Iterate through file handle and populate list of movies.
    for movie in fh_in:
        movies.append(movie)

    fh_in.close()
    return movies


def display_movies(mlist, start=0, end=250):
    # Iterate through file-handle and populate movie_list.
    idx = 1
    for movie in mlist:
        if idx >= int(start) and idx <= int(end):
            print(idx, movie, end="")
        idx += 1

    return None


movies = get_movies(file)

while True:
    print(menu)
    option = input("Enter option (1-4,q/Q=quit): ")
    if option == "1":
        display_movies(movies)
    elif option == "2":
        top_n = int(input("Choose (1-250): "))
        display_movies(movies, 0, top_n)
    elif option == "3":
        start_n = input("Choose start (1-250): ")
        end_n = input("Choose end (" +start_n + "-250): ")
        display_movies(movies, start_n, end_n)
    elif option == "4":
        r_num = random.randint(1, 250)
        display_movies(movies, r_num, r_num)
    elif option.lower() == "q":
        break
    else:
        print("Invalid option")

print("Done")