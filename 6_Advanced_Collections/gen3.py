#! /bin/python
# Name:        gen3.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Floating point version of the built-in range()
# function. Improved version using Decimal module.
"""
    Generate a sequence of accurate floating point numbers.
    frange([start,] stop, [step=0.25])
"""
import sys
import decimal

def frange(start, stop=None, step=0.25):
    """ Generate a sequence of floating point numbers """
    if step == 0: return []
    step = decimal.Decimal(str(step))

    if stop == None:
        stop = decimal.Decimal(str(start))
        curr = decimal.Decimal(0)
    else:
        stop = decimal.Decimal(str(stop))
        curr = decimal.Decimal(str(start))

    while curr < stop:
        yield float(curr)
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