#! /bin/python
# Name:        lotto.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Generates 6 Random Unique Lottery numbers.
"""
    Lottery number generator. Good luck and remember your trainer!
"""

import sys
import random

 
def main():
    """ The Main Program """
    lotto = set()  # Did we mention we want Unique numbers!
    while len(lotto) < 6:
        num = random.randint(1, 50)
        lotto.add(num)

    print(f"Lottery numbers = {lotto}")


if __name__ == "__main__":
    main()
    sys.exit(0)
