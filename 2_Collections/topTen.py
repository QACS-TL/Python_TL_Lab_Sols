#! /bin/python
# Name:        topTen.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Display top movies.
"""
    Top movies and Rankings.
"""
import sys

def main():
    movies = []

    fh_in = open(r"C:\labs\top250_movies.txt", mode="rt")
    movies = fh_in.readlines()  # Read movies into list.
    fh_in.close()


    ranky = 1
    for movie in movies:
        print(f"{ranky:>6d}: {movie}", end="")
        ranky += 1
        if ranky == 11:
            break

    for rank, movie in enumerate(movies, start=1):
        print(f"{rank:>6d}: {movie}", end="")
        if rank==10: break

    print(f"First movie = {movies[0]}", end="")
    print(f"Last movie = {movies[-1]}", end="")

    topN = int(input("Choose Top-N movies: "))
    for rank, movie in enumerate(movies, start=1):
        print(f"{rank:>6d}: {movie}", end="")
        if rank==topN: break
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
