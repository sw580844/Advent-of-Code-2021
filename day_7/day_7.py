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
    "16,1,2,0,4,2,7,1,2,14"
]

def fuel_to_align_to_point(crabs, point):
    """
    Given a list of crab positions, and a point to align to, calculate total fuel required
    """
    result = np.sum(np.abs(np.array(crabs) - point))

    return result

def calculate_cheapest_alignment_posn(crabs):
    """
    Given list of crabs, find (fuel) cheapest alignment position, and fuel cost of that position

    Returns cheapest alignment position, and fuel cost

    Args:
        - crabs : List of crab positions
    """

    cheapest_pos = None
    cheapest_fuel = np.inf
    for posn in range(np.min(crabs), np.max(crabs)):
        this_fuel = fuel_to_align_to_point(crabs, posn)
        if this_fuel < cheapest_fuel:
            cheapest_pos = posn
            cheapest_fuel = this_fuel
    return cheapest_pos, cheapest_fuel

def fuel_to_align_to_point_2(crabs, point):
    """
    Part 2 fuel calculation

    Fuel calculation not distance, but rather n(n+1)/2 , because it's a sum of 1 to move one unit,
    2 to move the second, 3 to move the third, etc thus to move n: 1 + 2 + .. + n
    """

    abs_deltas = np.abs(np.array(crabs) - point)
    costs = abs_deltas * (abs_deltas + 1)
    result = np.sum(costs)
    return result

def calculate_cheapest_alignment_posn_2(crabs):
    """
    For part 2, with different fuel costs.

    Given list of crabs, find (fuel) cheapest alignment position, and fuel cost of that position

    Returns cheapest alignment position, and fuel cost

    Args:
        - crabs : List of crab positions
    """
    candidate_posns = np.arange(np.min(crabs), np.max(crabs))
    fuel_costs = [fuel_to_align_to_point_2(crabs, i) for i in candidate_posns]
    return candidate_posns[np.argmin(fuel_costs)], np.min(fuel_costs)



def main():
    """
    Main entry point
    """

    test_values = [int(i) for i in TEST_DATA[0].split(",")]
    with open(INPUT_PATH, 'r', encoding="utf-8") as a_file:
        input_state = [int(i) for i in next(a_file).split(",")]


    print("Part 1:")
    test_result = fuel_to_align_to_point(test_values, 2)
    print(f"To align all test data to posn 2: {test_result}")
    cheapest_pos, cheapest_fuel = calculate_cheapest_alignment_posn(test_values)
    print(
        f"Part 1, Test data: cheapest position to align to, and fuel req: {cheapest_pos}, {cheapest_fuel}"
    )

    cheapest_pos, cheapest_fuel = calculate_cheapest_alignment_posn(input_state)
    print(
        f"Part 1, Input data: cheapest position to align to, and fuel req: {cheapest_pos}, {cheapest_fuel}"
    )

    # Part 2:
    print("Part 2")
    test_result = fuel_to_align_to_point_2(test_values, 5)
    print(f"Fuel to align test data to position 5: {test_result}")
    cheapest_pos, cheapest_fuel = calculate_cheapest_alignment_posn_2(test_values)
    print(
        f"Part 2, Test data: cheapest position to align to, and fuel req: {cheapest_pos}, {cheapest_fuel}"
    )

    cheapest_pos, cheapest_fuel = calculate_cheapest_alignment_posn_2(input_state)
    print(
        f"Part 2, Input data: cheapest position to align to, and fuel req: {cheapest_pos}, {cheapest_fuel}"
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
