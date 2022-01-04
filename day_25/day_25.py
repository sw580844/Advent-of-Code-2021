"""
SW 2022-01-04 Advent of code day 25

https://adventofcode.com/2021/day/25

This is just a conway game of life thing?

Performance enhancements, instead of value by value do entire at once?
Create mask of empty sites, use that, instead of value by value checks
"""

import os
import sys
import datetime


import numpy as np

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "v...>>.vv>",
    ".vv>>.vv..",
    ">>.>v>...v",
    ">>v>>.>.v.",
    "v>v.vv.v..",
    ">.>>..v...",
    ".vv..>.>v.",
    "v.v..>>v.v",
    "....v..v.>",
]

def parse_data(lines):
    """
    
    """

    result = []
    for line in lines:
        this_line_parsed = []
        for this_char in line:
            if this_char == "v":
                this_line_parsed.append(1)
            elif this_char == ".":
                this_line_parsed.append(0)
            elif this_char == ">":
                this_line_parsed.append(2)
            else:
                raise ValueError
        result.append(this_line_parsed)
    result = np.array(result, dtype=int)
    return result

def print_grid(grid):
    """
    
    """
    for row in grid:
        for value in row:
            if value == 0:
                print(".", end="")
            elif value == 1:
                print("v", end="")
            elif value == 2:
                print(">", end="")
            else:
                raise ValueError
        print("")
    return

def update_grid(grid):
    """
    Creates grid after one step
    """
    # Create a temp grid of input, as we'll move all the rightgoing cucumbers at once then downgoing
    temp_grid = grid.copy()
    result = np.zeros_like(grid)
    # Do right going, then down going
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if temp_grid[i,j] == 0:
                # Nothing here
                pass
            elif temp_grid[i,j] == 1:
                # Downward moving cucumber, check if space exists. Periodic BC!
                result[i,j] = 1
            elif temp_grid[i,j] == 2:
                # Rightward moving
                new_coord = i, (j+1) % temp_grid.shape[1]
                if temp_grid[new_coord[0], new_coord[1]] == 0:
                    result[new_coord[0], new_coord[1]] = 2
                    result[i,j] = 0
                else:
                    result[i,j] = 2
            else:
                raise ValueError
    # Down going, use prev result as the input so they all move simult. 
    temp_grid = result.copy()
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if temp_grid[i,j] == 0:
                # Nothing here
                pass
            elif temp_grid[i,j] == 1:
                # Downward moving cucumber, check if space exists. Periodic BC!
                new_coord = (i+1) % temp_grid.shape[0], j
                if temp_grid[new_coord[0], new_coord[1]] == 0:
                    result[i,j] = 0
                    result[new_coord[0], new_coord[1]] = 1
                else:
                    result[i,j] = 1
            elif temp_grid[i,j] == 2:
                # Rightward moving
                pass
            else:
                raise ValueError
    return result

def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    test_grid = parse_data(TEST_DATA)
    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]
    input_grid = parse_data(input_lines)
    print("Test data, zero updates")
    print_grid(test_grid)
    print("")
    this_grid = update_grid(test_grid)
    counter = 1
    # Run until the system halts
    while True:
        counter = counter + 1
        print(f"Test data, after {counter} updates:")
        print_grid(this_grid)
        print("")
        old_grid = this_grid.copy()
        this_grid = update_grid(this_grid)
        if (this_grid == old_grid).all():
            break
    # Run on input data:
    this_grid = update_grid(input_grid)
    counter = 1
    # Run until the system halts
    while True:
        counter = counter + 1
        print(f"Input data, {counter} updates")
        old_grid = this_grid.copy()
        this_grid = update_grid(this_grid)
        if (this_grid == old_grid).all():
            break
    print(f"Input data, halts after {counter} runs")
    






    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()