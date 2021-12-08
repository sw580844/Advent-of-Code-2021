"""
SW 2021-12-05 Advent of code day 5

https://adventofcode.com/2021/day/5
"""

import os
import sys
import re
import pprint

import numpy as np


INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

def main():
    """
    
    """

    

    MAX_DIM = 10
    grid = np.zeros((MAX_DIM, MAX_DIM))
    value_regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)\n?")
    # Draw lines into grid
    for line in TEST_DATA:
        match_result = value_regex.match(line)
        values = [int(i) for i in match_result.groups()]
        # Only doing horizontal or vertical at the moment
        if values[0] != values[2] and values[1] != values[3]:
            continue
        start = np.array(values[:2])
        end = np.array(values[2:])
        delta = (end - start)
        unit_delta = (delta / np.linalg.norm(delta)).astype(int)
        covered = 0
        this_pt = start
        while covered <= np.linalg.norm(delta):
            grid[this_pt[0], this_pt[1]] = grid[this_pt[0], this_pt[1]] + 1
            this_pt = this_pt + unit_delta
            covered = covered + 1
        print(grid)
        
    print("Test data: Number covered by two lines: {}".format(len(grid[grid > 1])))
    print(grid)

    # Now do the input
    MAX_DIM = 1000
    grid = np.zeros((MAX_DIM, MAX_DIM))
    value_regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)\n?")
    # Draw lines into grid
    # with open(INPUT_PATH, 'r') as a_file:
    #     lines = [i.rstrip('\n') for i in a_file]
    
    # for line in lines:
    #     match_result = value_regex.match(line)
    #     values = [int(i) for i in match_result.groups()]
    #     # Only doing horizontal or vertical at the moment
    #     if values[0] != values[2] and values[1] != values[3]:
    #         continue
    #     start = np.array(values[:2])
    #     end = np.array(values[2:])
    #     delta = (end - start)
    #     unit_delta = (delta / np.linalg.norm(delta)).astype(int)
    #     covered = 0
    #     this_pt = start
    #     while covered <= np.linalg.norm(delta):
    #         grid[this_pt[0], this_pt[1]] = grid[this_pt[0], this_pt[1]] + 1
    #         this_pt = this_pt + unit_delta
    #         covered = covered + 1
        
        
    # print("Input data: Number covered by two lines: {}".format(len(grid[grid > 1])))

    # Second part: now consider diagonal lines
    print("Part 2:")
    MAX_DIM = 10
    grid = np.zeros((MAX_DIM, MAX_DIM))
    value_regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)\n?")
    # Draw lines into grid
    for line in TEST_DATA:
        match_result = value_regex.match(line)
        values = [int(i) for i in match_result.groups()]
        
        start = np.array(values[:2])
        end = np.array(values[2:])
        dx = end[1] - start[1]
        dy = end[0] - start[0]

        this_type = None
        if abs(dx) == abs(dy):
            this_type = "diag"
        elif dx == 0 and dy != 0:
            this_type = "vert"
        elif dx != 0 and dy == 0:
            this_type = "horz"
        else:
            raise ValueError
        # print(this_type)
        

        this_pt = start
        # Turn to unit deltas
        dx = np.sign(dx) * 1
        dy = np.sign(dy) * 1
        # print(f"dx {dx} dy {dy}")
        
        while (this_pt != end).any():
            print(values, this_pt)
            y, x = this_pt
            grid[y, x] = grid[y, x] + 1

            this_pt = this_pt + np.array([dy, dx])
        # Draw final point
        grid[end[0], end[1]] = grid[end[0], end[1]] + 1

        # print(grid)
        
    print("Test data: Number covered by two lines: {}".format(len(grid[grid > 1])))
    print(grid)

    # Run on input data
    MAX_DIM = 1000
    grid = np.zeros((MAX_DIM, MAX_DIM))
    value_regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)\n?")
    with open(INPUT_PATH, 'r') as a_file:
        lines = [i.rstrip('\n') for i in a_file]
    
    for line in lines:
        match_result = value_regex.match(line)
        values = [int(i) for i in match_result.groups()]
        
        start = np.array(values[:2])
        end = np.array(values[2:])
        dx = end[1] - start[1]
        dy = end[0] - start[0]

        this_type = None
        if abs(dx) == abs(dy):
            this_type = "diag"
        elif dx == 0 and dy != 0:
            this_type = "vert"
        elif dx != 0 and dy == 0:
            this_type = "horz"
        else:
            raise ValueError
        # print(this_type)
        

        this_pt = start
        # Turn to unit deltas
        dx = np.sign(dx) * 1
        dy = np.sign(dy) * 1
        # print(f"dx {dx} dy {dy}")
        
        while (this_pt != end).any():
            # print(values, this_pt)
            y, x = this_pt
            grid[y, x] = grid[y, x] + 1

            this_pt = this_pt + np.array([dy, dx])
        # Draw final point
        grid[end[0], end[1]] = grid[end[0], end[1]] + 1

        # print(grid)
    print("Input data: Number covered by two lines: {}".format(len(grid[grid > 1])))

    sys.exit(0)

if __name__ == "__main__":
    main()