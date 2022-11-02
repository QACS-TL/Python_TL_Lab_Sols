#! /bin/python
# Name:        test_movieDB.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Instantiate and test our MovieDB objects.
"""
    Store and Retrieve movie data to dB using a MovieDB object.
"""

import sys
import movieDB

def main():
    """ The Main Program """
    movies = movieDB.MovieDB() # Instantiate MovieDB object.
    movies.create_table()
    movies.insert_row(1, 'Brave', '2012', 10)
    movies.insert_row(2, 'Braveheart', '1995', 10)
    movies.insert_row(3, 'Babe', '1995', 10)
    movies.commit()
    movies.query_all_rows()
    movies.delete_row(1)
    movies.delete_row(2)
    movies.delete_row(3)
    movies.commit()

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)