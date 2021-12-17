"""
SW 2021-12-15 Advent of code day 15

https://adventofcode.com/2021/day/15
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
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

def parse_data(lines):
    """
    Parse data to grid
    """
    grid = []
    for line in lines:
        grid.append([int(i) for i in line])
    grid = np.array(grid)
    return grid

def compute_minimum_danger_path_grid(grid):
    """
    Create a grid showing the minimum summed danger to reach the bottom right

    Upon reflection, this assumes that loops aren't likely
    """

    result = np.zeros_like(grid)


    for row_idx in range(1, result.shape[0]*2):
        for col_idx in range(0, row_idx+1):
            # print(f"{row_idx - col_idx}, {col_idx}")
            i, j = row_idx - col_idx, col_idx
            if i < 0 or i >= result.shape[0]:
                continue
            if j < 0 or j >= result.shape[1]:
                continue
            neighbours = []
            if i - 1  >= 0:
                neighbours.append([i-1, j])
            if j - 1 >= 0:
                neighbours.append([i, j-1])
            neighbour_vals = [result[i, j] for (i,j) in neighbours]
            result[row_idx - col_idx, col_idx] = min(neighbour_vals) + grid[row_idx - col_idx, col_idx]

    return result

def compute_min_danger_path_grid_2(grid):
    """
    Second way to construct minimum path grid, this brute forces and iterates over every array
    element until there's no change between steps

    """
    # Default state, -1
    old_result = np.zeros_like(grid) -1
    old_result[0,0] = 0

    # In a while loop, continuously update until finished
    counter = 0
    while True:
        print(f"Counter: {counter}")
        new_result = old_result.copy()
        for i in range(0, new_result.shape[0]):
            for j in range(0, new_result.shape[1]):
                if i == 0 and j == 0:
                    continue
                neighbours = [
                    [i-1, j],
                    [i+1, j],
                    [i, j-1],
                    [i, j+1]
                ]
                neighbours = [(a,b) for (a,b) in neighbours if 0 <= a < new_result.shape[0]]
                neighbours = [(a,b) for (a,b) in neighbours if 0 <= b < new_result.shape[1]]
                neighbour_vals = [new_result[a, b] for (a,b) in neighbours]
                neighbour_vals = [i for i in neighbour_vals if i > -1]
                # print(i, j, neighbours)
                new_result[i,j] = min(neighbour_vals) + grid[i,j]
        counter = counter + 1
        if (new_result == old_result).all():
            # Break if no change
            break
        else:
            # Set result to old result and start again
            old_result = new_result
    return new_result


def print_grid(grid):
    """
    Quick func to print the grid out
    """
    print(grid.shape)
    for row in grid:
        for element in row:
            print("{:02d},".format(element), end="")
        print("")
    return

def expand_grid(grid):
    """
    For part 2, we copy the original grid 5 times in horz and vert, and +1 each time
    Values > 9 wrap around to 1
    """
    result = np.zeros((grid.shape[0] * 5, grid.shape[1] * 5), dtype=int)
    orig_rows = grid.shape[0]
    orig_cols = grid.shape[1]
    for i in range(0, 5):
        for j in range(0, 5):
            this_section = grid + (i+j)
            # Wrap around
            func = np.vectorize(lambda x: x if x < 10 else x % 9)
            # this_section[this_section > 9] = this_section % 9
            this_section = func(this_section)
            # Now paste in
            result[i * orig_rows:(i+1) * orig_rows, j * orig_cols:(j+1) * orig_cols] = this_section
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

    min_danger_path_grid = compute_minimum_danger_path_grid(test_grid)
    print("Test data: Grid of minimum danger to reach point:")
    print(min_danger_path_grid[-1, -1])


    result = compute_min_danger_path_grid_2(test_grid)
    print_grid(result)

    min_danger_path_grid = compute_minimum_danger_path_grid(input_grid)
    print(f"Erroneous result for input data: {min_danger_path_grid[-1, -1]}")
    min_danger_path_grid = compute_min_danger_path_grid_2(input_grid)
    print("Input data: Grid of minimum danger to reach point:")
    print(min_danger_path_grid[-1, -1])

    # Part 2: the grid is expanded
    print("Part 2:")
    expanded_test = expand_grid(test_grid)
    expanded_input = expand_grid(input_grid)

    min_danger_path_grid = compute_min_danger_path_grid_2(expanded_test)
    print(f"Test data: Minimum danger path {min_danger_path_grid[-1,-1]}")
    min_danger_path_grid = compute_min_danger_path_grid_2(expanded_input)
    print(f"Input data: Minimum danger path {min_danger_path_grid[-1,-1]}")

    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
