"""
SW 2021-12-08 Advent of code day 8

https://adventofcode.com/2021/day/8
"""

import os
import sys
import re

import numpy as np



INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]

def parse_data(lines):
    """
    Given test lines, work out grid and rules
    """
    idxs = []
    rules = []
    gather_rules = False
    for line in lines:
        if line == "":
            gather_rules = True
            continue
        if not gather_rules:
            idxs.append([int(i) for i in line.split(",")])
        else:
            rules.append(line)
    # Add 1 to get final values
    # Idxs given as (x,y)
    dims = np.max([i[1] for i in idxs])+1, np.max([i[0] for i in idxs])+1
    grid = np.zeros(dims, dtype=int)
    for (x,y) in idxs:
        grid[y,x] = 1
    return grid, rules

def print_grid(grid):
    """
    Quick function to print grid similar to advent of code website
    """
    for i in range(0, grid.shape[0]):
        for j in range(0, grid.shape[1]):
            if grid[i,j] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    return

def fold_grid(grid, rule):
    """
    Given a grid of values (one hot) and a list of textual folding rules, perform the folds as 
    requested
    """
    rule_regex = re.compile(r"fold along ([x|y])=(\d+)")
    dimension, value = rule_regex.match(rule).groups()
    value = int(value)

    if dimension == "x":
        new_dimensions = grid.shape[0], value
    elif dimension == "y":
        new_dimensions = value, grid.shape[1]
    else:
        raise ValueError

    result = np.zeros(new_dimensions, dtype=int)
    for i in range(0, new_dimensions[0]):
        for j in range(0, new_dimensions[1]):
            if dimension == "y":
                idx_of_folded = [2*value - i, j]
            elif dimension == "x":
                idx_of_folded = [i, 2*value - j]
            else:
                raise ValueError
            check_col_idx = idx_of_folded[0] >= 0 and idx_of_folded[0] < grid.shape[0]
            check_row_idx = idx_of_folded[1] >= 0 and idx_of_folded[1] < grid.shape[1]
            if check_col_idx and check_row_idx:
                folded_value = grid[idx_of_folded[0], idx_of_folded[1]]
            else:
                folded_value = 0

            result[i,j] = grid[i,j] + folded_value
    # Make 1 hot
    result[result > 1] = 1
    return result


def main():
    """
    Main entry point
    """
    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]

    test_grid, test_rules = parse_data(TEST_DATA)
    print_grid(test_grid)
    print("")

    result = fold_grid(test_grid, test_rules[0])
    print("")
    result = fold_grid(result, test_rules[1])
    print("Test data: Dots present: {}".format(len(result[result>0])))

    input_grid, input_rules = parse_data(input_lines)
    result = fold_grid(input_grid, input_rules[0])
    print("Input data: Dots present: {}".format(len(result[result>0])))

    for rule in input_rules[1:]:
        result = fold_grid(result, rule)
    print_grid(result)


    sys.exit(0)

if __name__ == "__main__":
    main()
