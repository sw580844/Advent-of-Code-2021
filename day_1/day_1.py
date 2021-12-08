"""
SW 2021-12-04 Advent of code day 1

https://adventofcode.com/2021/day/1
"""

import os
import sys

import numpy as np

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

def main():
    """
    Main entry point
    """
    # Part one: increasing from one value to the next
    input_data = np.genfromtxt(INPUT_PATH)

    number_increasing = sum(np.diff(TEST_DATA) > 0)
    print(f"Test data: number increasing: {number_increasing}")
    number_increasing = sum(np.diff(input_data) > 0)
    print(f"Number of increasing steps: {number_increasing}")

    print("Part 2:")
    # Part two: use three element groups, we'll do with a convo
    convolved = np.convolve(TEST_DATA, [1,1,1], mode="valid")
    number_increasing = np.sum(np.diff(convolved) > 0)
    print(f"Number increasing in test data: {number_increasing}")
    convolved = np.convolve(input_data, [1,1,1], mode="valid")
    number_increasing = np.sum(np.diff(convolved) > 0)
    print(f"Number increasing in supplied data: {number_increasing}")

    sys.exit(0)

if __name__ == "__main__":
    main()
