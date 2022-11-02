#! /bin/python
# Name:        gen.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Floating point version of the built-in range()
# function.
"""
    Generate a sequence of floating point numbers.
    frange(start, stop, [step=0.25])
"""
import sys

def frange(start, stop, step=0.25):
    """ Generate a sequence of floating point numbers """
    if step == 0: return []

    curr = float(start)
    while curr < stop:
        yield round(curr, 2)
        curr += step

def main():
    """ The Main Program """
    print(list(frange(1.1, 3)))
    print(list(frange(1, 3, 0.33)))
    print(list(frange(1, 3, 1))) # Should return [1.0, 2.0], not [1, 2]
    print(list(frange(3, 1))) # Should return an empty list
    print(list(frange(1, 3, 0))) # Should return an empty list
    print(list(frange(-1, -0.5, 0.1)))
    print(frange(1,2)) # Should print <generator object frange at 0x..

    for num in frange(3.142, 12):
        print(f"{num:05.2f}")
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)