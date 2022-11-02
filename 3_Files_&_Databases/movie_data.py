#! /bin/python
# Name:        movie_data.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Write detailed movie information to file.
"""
    Persistent Movie Information.
"""

import sys

def main():
    movies = [{"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
              {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
              {"title": "The Godfather; Part II", "director": "Francis Ford Coppola", "year": 1974},
              {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008},
              {"title": "12 Angry Men", "director": "Sidney Lumet", "year": 1957}
              ]

    fh_out = open(r"C:\labs\top5_movie_info.txt", mode="wt")

    for movie in movies:
        print(f"{movie['year']:>10} - "
              f"Title:{movie['title'].title():<30s}"
              f"Director:{movie['director']:>25s}", file=fh_out)

    fh_out.close()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)