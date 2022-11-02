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

def main():
    ia = imdb.IMDb()
    count = 0
    # regexcomp = re.compile(r"[aeiou]{3}")
    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        pattern = r"^the" # 50 lines.
        # pattern = r"[0-9]"  # 11 lines.
        # pattern = r".*[aeiou]{3}"  # 5 lines.
        # pattern = r"^(.).*\1$" # 15 lines.
        # pattern = r"^[^a-zA-Z]+$"  # 1 line.
        # pattern = r"monty"  # 1 lines.
        # pattern = r"\s+(\w+)\s+.*\1\s+"  # 8 lines.

        m = re.search(pattern, str(movie), re.IGNORECASE)
        # m = regexcomp.match(str(movie), re.IGNORECASE)
        if m:
            print(f"{rank:>4}: {movie}")
            count += 1
    print(f"Matched {count} lines")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)