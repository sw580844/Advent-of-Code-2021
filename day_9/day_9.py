"""
SW 2021-12-05 Advent of code day 6

https://adventofcode.com/2021/day/6
"""

import os
import sys

import numpy as np

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]

def make_grid(lines):
    """
    Make a numpy 2D array from lines of values
    """
    result = np.array([list(map(int, line)) for line in lines])

    return result

def local_min_map(grid):
    """
    Given a grid, return a boolean array corresponding to local minima
    """
    down_change = np.ones_like(grid)
    down_change[:-1, :] = grid[1:, :] - grid[:-1, :]
    right_change = np.ones_like(grid)
    right_change[:, :-1] = grid[:, 1:] - grid[:, :-1]
    up_change = np.ones_like(grid)
    up_change[1:, :] = grid[:-1, :] - grid[1:, :]
    left_change = np.ones_like(grid)
    left_change[:, 1:] = grid[:, :-1] - grid[:, 1:]

    result = (up_change > 0) & (down_change > 0) & (left_change > 0) & (right_change > 0)
    return result

def find_basin(grid):
    """
    Now we need to find basins within the grid
    """

    return

def main():
    """
    Main entry point
    """

    with open(INPUT_PATH, 'r') as a_file:
        lines = [i.rstrip("\n") for i in a_file if i != "\n"]
    input_grid = make_grid(lines)

    test_grid = make_grid(TEST_DATA)
    print("Part 1")
    print("Test grid, test grid shape:")
    print(test_grid, test_grid.shape)

    test_minima = local_min_map(test_grid)
    print("Local minima in test grid:")
    print(test_minima)
    minima_values = test_grid[test_minima]
    print(f"Test data: Minima values: {minima_values}")
    print(f"Test data: Submission: {np.sum(minima_values + 1)}")

    input_minima = local_min_map(input_grid)
    minima_values = input_grid[input_minima]
    print(f"Input data: submission: {np.sum(minima_values + 1)}")

    print("Part 2:")



    sys.exit(0)

if __name__ == "__main__":
    main()
