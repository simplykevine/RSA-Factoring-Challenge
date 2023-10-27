#!/usr/bin/python3
"""Module that factorise all numbers it should into a product of two smaller numbers."""

import sys
import time
import math

def factorize_number(num):
    factors = []
    divisor = 2

    while num > 1:
        if num % divisor == 0:
            factors.append(str(divisor))
            num //= divisor

        else:
            divisor += 1

    return '*'.join(factors)
""""print out a simple decomposition of an integer """


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 factors.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factorization = factorize_number(number)
                print(f"{number}={factorization}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid format. file must contains only natural numbers.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
