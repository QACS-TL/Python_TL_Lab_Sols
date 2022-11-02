#! /bin/python
# Name:        calc.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: A Calculator program
"""
    Calculator program with add, divide, multiply,
    subtract and modulus functionality.
"""
import sys

# def add(x, z):
#    """ Return sum of x and z """
#    return x + z

def divide(x, z):
    """ Return x divided by z to 3 decimal places """
    return x/z

# def multiply(x, z):
#     """ Return product of x and z """
#    return x * z

def subtract(x, z):
    """ Return difference of x and z  """
    return x - z

def modulus(x, z):
    """ Return remainder of x divided by z """
    return x % z

# Solution for Part 3
def add(*numbers):
   """ Return sum of all parameters """
   return sum(numbers)

def multiply(*numbers):
   """ Return the product of all parameters """
   product = 1
   for num in numbers:
       product *= num
   return product

def main():
    """ This is the main program function """
    print(f"11 + 5 = {add(11, 5)}")
    print(f"11 / 5 = {divide(11, 5)}")
    print(f"11 * 5 = {multiply(11, 5)}")
    print(f"11 - 5 = {subtract(11, 5)}")
    print(f"11 % 5 = {modulus(11, 5)}")

    print(f"11 + 5 + 33 + 15 + 6.5 = {add(11, 5, 33, 15, 6.5)}")
    print(f"11 * 5 * 33 * 15 * 6.5 = {multiply(11, 5, 33, 15, 6.5)}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
