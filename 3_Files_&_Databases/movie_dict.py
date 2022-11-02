#! /bin/python
# Name:        movie_dict.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Preserve Movie dictionary to file.
"""
    Preserving Movie information.
"""

import sys
import pickle
import gzip
import pprint

def main():
    movies = [{"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
              {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
              {"title": "The Godfather; Part II", "director": "Francis Ford Coppola", "year": 1974},
              {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008},
              {"title": "12 Angry Men", "director": "Sidney Lumet", "year": 1957}
              ]

    # Open compressed file handle for writing in Binary mode.
    fh_out = gzip.open(r"C:\labs\top5movies.pgz", mode="wb")
    pickle.dump(movies, fh_out)
    fh_out.close()

    # Open compressed file handle for writing in Binary mode.
    fh_in = gzip.open(r"C:\labs\top5movies.pgz", mode="rb")
    films = pickle.load(fh_in)
    fh_in.close()

    pprint.pprint(movies)
    print("-" * 60)
    pprint.pprint(films)
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
