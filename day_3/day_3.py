"""
SW 2021-12-04 Advent of code day 2

https://adventofcode.com/2021/day/3
"""

import os
import sys
import operator


INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

def calc_rates(input_data):
    """
    Calculate the gamma rate


    """
    gamma_result = 0
    epsilon_result = 0
    for i in range(0, len(input_data[0])):
        gamma_result = gamma_result << 1
        epsilon_result = epsilon_result << 1
        this_bit_high = len([1 for j in input_data if j[i] == "1"]) > (0.5 * len(input_data))
        if this_bit_high:
            gamma_result = gamma_result + 1
        else:
            epsilon_result = epsilon_result + 1
    return gamma_result, epsilon_result

def calc_oxygen_rating(input_data):
    """
    Calculate oxygen rating
    """
    oxygen_rating = 0
    
    data = input_data
    for i in range(0, len(input_data[0])):
        number_high = len([1 for j in data if j[i] == "1"])
        if number_high >= 0.5 * len(data):
            data = [j for j in data if j[i] == "1"]
        else:
            data = [j for j in data if j[i] == "0"]
        if len(data) == 1:
            oxygen_rating = int(data[0], base=2)
            break
    return oxygen_rating

def calc_scrubber_rating(input_data):
    """
    Calc scrubber rating
    """
    result = 0
    data = input_data
    for i in range(0, len(input_data[0])):
        number_high = len([1 for j in data if j[i] == "1"])
        if number_high >= 0.5 * len(data):
            data = [j for j in data if j[i] == "0"]
        else:
            data = [j for j in data if j[i] == "1"]
        if len(data) == 1:
            result = int(data[0], base=2)
            break
    return result


def main():
    """
    Main entry point
    """
    with open(INPUT_PATH, 'r', encoding="utf-8") as a_file:
        input_data = a_file.readlines()
    # Remove newlines
    input_data = [i.rstrip('\n') for i in input_data]

    # Part 1:
    # Bit of a hack here because we don't have a pretold fixed width for rates, so calc twice
    print("Part 1")
    gamma_rate, epsilon_rate = calc_rates(TEST_DATA)
    print(f"Test data gamma rate: {gamma_rate}, epsilon rate {epsilon_rate}, product {gamma_rate * epsilon_rate}")
    gamma_rate, epsilon_rate = calc_rates(input_data)
    print(f"Input data gamma rate {gamma_rate}, epsilon rate {epsilon_rate}, product {gamma_rate * epsilon_rate}")

    # Part 2:
    print("Part 2")
    oxygen_rating = calc_oxygen_rating(TEST_DATA)
    scrubber_rating = calc_scrubber_rating(TEST_DATA)
    print(f"Test oxygen rating : {oxygen_rating}, scrubber rating {scrubber_rating}")
    print(f"Test life support rating {oxygen_rating * scrubber_rating}")
    oxygen_rating = calc_oxygen_rating(input_data)
    scrubber_rating = calc_scrubber_rating(input_data)
    print(f"Input data oxygen rating : {oxygen_rating}, scrubber rating {scrubber_rating}")
    print(f"Input data life support rating {oxygen_rating * scrubber_rating}")




    sys.exit(0)

if __name__ == "__main__":
    main()