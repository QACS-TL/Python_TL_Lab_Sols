#! /bin/python
# Name:        top250.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Download the top 250 movies chosen by IMDb users.
"""
    Download and display online movie information.
"""
import sys

def main():
    fh_in = open(r"C:\labs\top250_movies.txt", mode="rt")
    for movie in fh_in:
        print(f"{movie.title()}", end="")
    fh_in.close()

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)