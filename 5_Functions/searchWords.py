#! /bin/python
# Name:        searchWords.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Search and display lines in multiple files using
# Regular expressions
"""
    Pattern searching Tool
"""

import sys
import re

def search_pattern(pattern, *files):
    """ Search for Regex patterns in multiple file/s """
    if not files:
        files = [r"C:\labs\words"]
    for file in files:
        fh_in = open(file, mode="rt")
        for line in fh_in:
            m = re.search(pattern, line)
            if m:
                print(line, end="")

        fh_in.close()

    return None

def main():
    """ Main Program """
    search_pattern(r"^([A-Z]).*\1$")
    # search_pattern(r"^([A-Z]).*\1$", r"C:\labs\words", r"C:\labs\words")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)