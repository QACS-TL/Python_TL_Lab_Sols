#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will demonstrate how to match string
# data using Regular Expressions and pre-compiling the pattern once.
"""
    Search a given file using regular expressions and display
    matched lines.
"""
import sys
import re

def search_pattern(pattern, *files):
    """ Display lines in a given file which match 4_Regular_Expressions """
    if len(files) == 0:
        files = (r"C:\labs\words",)

    for file in files:
        fh_in = open(file, mode="rt")

        # Iterate through file handle
        for line in fh_in:
            # Pre-compiled pattern stored in reobj object.
            m = re.search(pattern, line) # Return None or RE Match object.
            if m:
                print(line, end="")

        fh_in.close()
    return None

def main():
    """ Demonstrate different 4_Regular_Expressions patterns """
    search_pattern(r"^([A-Z]).*\1$")
    search_pattern(r"^([A-Z]).*\1$", r"C:\labs\words", r"C:\labs\words")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
