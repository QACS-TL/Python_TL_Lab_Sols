#! /bin/python
# Name:        topTen_stretch.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Display top movies.
"""
    Top movies and Rankings.
"""
import sys

def get_movies():
    fh_in = open(r"C:\labs\top250_movies.txt", mode="rt")
    movies = fh_in.readlines()
    fh_in.close()
    return movies

def display_movies(movies, topN):
    for rank, movie in enumerate(movies, start=1):
        print(f"{rank:>6d}: {movie}", end="")
        if rank == topN: break
    return None

def search_movies(text, movies):
    for rank, movie in enumerate(movies, start=1):
        if text in movie:
            print(f"{rank:>6d}: {movie}", end="")
            return None
    print(f"{text} not found")
    return None

def main():
    movies = []
    while True:
        menu = """
            Menu Options
            ------------
            1. Get online movie ranking from IMDB
            2. Display top ranking movies
            3. Search for movie
        """
        print(menu)
        option = input("Enter option: ")
        if option == "1":
            movies = get_movies()
        elif option == "2":
            topN = int(input("Choose topN movies:"))
            display_movies(movies, topN)
        elif option == "3":
            text = input("Enter movie to search:")
            search_movies(text, movies)
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

