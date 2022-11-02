#! /bin/python
# Name:        gen2.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Floating point version of the built-in range()
# function. Improved version that can accept ONE parameter.
"""
    Generate a sequence of floating point numbers.
    frange([start,] stop, [step=0.25])
"""
import sys

def frange(start, stop=None, step=0.25):
    """ Generate a sequence of floating point numbers """
    if step == 0: return []
    if stop == None:
        stop = start
        curr = 0.0
    else:
        curr = float(start)

    while curr < stop:
        yield curr
        curr += step

def main():
    """ The Main Program """
    result1 = list(frange(0, 3.5, 0.25))
    result2 = list(frange(3.5))

    if result1 == result2:
        print("Default worked!")
    else:
        print("Oops! {result1} not equal to {result2}")

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)