#! /bin/python
# Name:        display_movies.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Display movie information
"""
    IMDB movie information
"""
import sys

def display_top250():
    """ Display top 250 movies """
    fh_in = open(r"C:\labs\top250_movies.txt", mode="rt")
    for rank, movie in enumerate(fh_in, start=1):
        print(f"{rank}. {movie.title()}", end="")
    fh_in.close()
    return None

def main():
    # Solution for Ques 2 & 3.
    display_top250()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)