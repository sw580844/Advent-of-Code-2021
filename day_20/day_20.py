"""
SW 2021-12-20 Advent of code day 20

https://adventofcode.com/2021/day/20
"""

import os
import sys
import datetime
import re

import numpy as np

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
    "",
    "#..#.",
    "#....",
    "##..#",
    "..#..",
    "..###",
]

def parse_data(lines):
    """
    
    """
    algorithm = lines[0]

    image_lines = lines[2:]
    image = np.zeros( (len(image_lines), len(lines[2])), dtype=int)
    
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if image_lines[i][j] == "#":
                image[i,j] = 1
            else:
                image[i,j] = 0
    return algorithm, image

def print_image(image):
    """
    
    """
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if image[i,j] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    return

def get_neighbour_bin(image, i, j):
    """
    Find neighbours of i,j
    """
    # pad image


    neighbourhood_bin = 0
    neighbourhood = []
    for idx in range(0, 9):
        this_i = (i-1) + idx // 3
        this_j = (j-1) + idx % 3
        this_val = image[this_i, this_j]
        neighbourhood_bin = (neighbourhood_bin << 1) + this_val
        neighbourhood.append(this_val)


    return neighbourhood_bin

def enchance_image(image, algorithm, background = 0):
    """
    
    """
    # pad image
    padding = 3
    new_size = (image.shape[0]+2*padding, image.shape[1]+2*padding)
    temp_image = np.zeros(new_size, dtype=int) + background
    temp_image[temp_image>1] = 1
    temp_image[padding:-padding, padding:-padding] = image

    # print_image(temp_image)
    # Deal with background
    # print(f"prev background: {background}, algorithm[0]: {algorithm[0]}")
    # print("Check")
    if background == 0 and algorithm[0] == "#":
        background = 1
    elif background == 1 and algorithm[-1] == ".":
        background = 0
    # print(f"Background: {background}")

    result = np.zeros_like(temp_image) + background
    result[result>1] = 1

    for i in range(1, result.shape[0]-1):
        for j in range(1, result.shape[1]-1):
            # print(i,j)
            neighbour_bin = get_neighbour_bin(temp_image, i, j)
            if algorithm[neighbour_bin] == "#":
                result[i,j] = 1
            else:
                result[i,j] = 0
    #

    return result, background

def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]

    test_algorithm, test_image = parse_data(TEST_DATA)
    input_algorithm, input_image = parse_data(input_lines)
    print("Test image:")
    print_image(test_image)

    # Do two level of enhancement
    print(f"Centre of test_image: {test_image[test_image.shape[0] // 2, test_image.shape[1] // 2]}")
    enhanced, background = enchance_image(test_image, test_algorithm)
    print(f"Test data: After one level of enhancement, {len(enhanced[enhanced>0])} pixels are lit")
    print(f"Centre of enhanced is: {enhanced[enhanced.shape[0]//2, enhanced.shape[1]//2]}")
    # After one level there should be 24
    print_image(enhanced)
    enhanced, background = enchance_image(enhanced, test_algorithm, background)
    print(f"Test data: After two levels of enhancement, {len(enhanced[enhanced>0])} pixels are lit")
    print_image(enhanced)

    # Now do on input
    print("Input:")
    # print_image(input_image)
    print(f"Starting, {len(input_image[input_image>0])} pixels are lit")
    enhanced, background = enchance_image(input_image, input_algorithm)
    print(f"Input data: After one level of enhancement, {len(enhanced[enhanced>0])} pixels are lit")
    # print_image(enhanced)
    enhanced, background = enchance_image(enhanced, input_algorithm, background)
    print(f"Input data: After two levels of enhancement, {len(enhanced[enhanced>0])} pixels are lit")
    # print_image(enhanced)
    
    print("Part 2:")
    # Yeah now it's do it a bunch of times
    enhanced, background = enchance_image(test_image, test_algorithm)
    for i in range(1, 3):
        print(f"Test data: After {i} enhancements, {len(enhanced[enhanced>0])} pixels are lit")
        enhanced, background = enchance_image(enhanced, test_algorithm, background)

    enhanced, background = enchance_image(input_image, input_algorithm)
    for i in range(1, 51):
        print(f"Input data data: After {i} enhancements, {len(enhanced[enhanced>0])} pixels are lit")
        enhanced, background = enchance_image(enhanced, input_algorithm, background)

    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
