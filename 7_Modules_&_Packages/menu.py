#! /bin/python
# Name:        menu.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Top level menu program.
"""
    Menu of reusable functions.
"""

import sys
from searchWords import search_pattern # Option 1.
from display_movies import display_top250 # Option 2.
from search250 import search_movie # Option 3.
from display_unused_ports import unused_ports # Option 4.

def main():
    """ The Main Program """
    menu = """
        Menu Options
        ------------
        1. Search for pattern in file
        2. Display top250 movies
        3. Search top250 movies
        4. Display unused ports
        
    """

    while True:
        print(menu)
        option = input("Enter option (1-4, q=quit): ")
        if option == "1":
            pattern = input("Enter search pattern: ")
            search_pattern(pattern)
        elif option == "2":
            display_top250()
        elif option == "3":
            pattern = input("Enter search pattern: ")
            search_movie(pattern)
        elif option == "4":
            unused_ports()
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
