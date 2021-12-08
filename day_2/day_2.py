"""
SW 2021-12-04 Advent of code day 2

https://adventofcode.com/2021/day/2
"""

import os
import sys
import operator


INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def calculate_new_position(commands):
    """
    Given list of string commands, work out new position
    """
    depth = 0
    horz = 0
    for command in commands:
        this_movement, value = command.split(" ")
        value = int(value)
        if this_movement == "forward":
            horz = horz + value
        elif this_movement == "down":
            depth = depth + value
        elif this_movement == "up":
            depth = depth - value
    return horz, depth


def calc_new_position_part_2(commands):
    """
    Now have to include aim value
    """
    depth = 0
    horz = 0
    aim = 0
    for command in commands:
        this_movement, value = command.split(" ")
        value = int(value)
        if this_movement == "forward":
            horz = horz + value
            depth = depth + aim  * value
        elif this_movement == "down":
            aim = aim + value
        elif this_movement == "up":
            aim = aim - value
    return horz, depth

def main():
    """
    Main entry point
    """
    with open(INPUT_PATH, 'r', encoding="utf-8") as a_file:
        input_data = a_file.readlines()

    # Part 1
    print("Part 1:")
    new_position = calculate_new_position(TEST_DATA)
    print("Test data position: {}, product {}".format(new_position, operator.mul(*new_position)))
    new_position = calculate_new_position(input_data)
    print("Input data position: {}, product {}".format(new_position, operator.mul(*new_position)))

    # Part 2
    print("Part 2:")
    new_position = calc_new_position_part_2(TEST_DATA)
    print("Test data position: {}, product {}".format(new_position, operator.mul(*new_position)))
    new_position = calc_new_position_part_2(input_data)
    print("Input data position: {}, product {}".format(new_position, operator.mul(*new_position)))


    sys.exit(0)

if __name__ == "__main__":
    main()
