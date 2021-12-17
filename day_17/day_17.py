"""
SW 2021-12-17 Advent of code day 17

https://adventofcode.com/2021/day/17
"""

import os
import sys
import datetime
import re



INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "target area: x=20..30, y=-10..-5",
]

def update_state(state):
    """
    state: (x, x', y, y')
    """
    x, v_x, y, v_y = state
    x = x + v_x
    y = y + v_y
    if v_x > 0:
        v_x = v_x - 1
    v_y = v_y - 1
    return x, v_x, y, v_y

def run_sim(initial_state, border_area):
    """
    Runs a simulation until we fall below the search area, or overshoot in horz
    Returns:
        found_search : bool, whether probe stopped in search area
        apex : apex/apogee, highest y value in trajectory
    """
    x, v_x, y, v_y = initial_state
    x_min, x_max, y_min, y_max = border_area
    found_search = False
    apex = 0
    while x <= x_max and y >= y_min:
        x, v_x, y, v_y = update_state([x, v_x, y, v_y])
        if y > apex:
            apex = y
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            found_search = True
            break

    return found_search, apex

def search_for_apex(v_x_min, v_x_max, v_y_min, v_y_max, search_border):
    """
    Finds highest apex that also includes stop in search border
    """
    best_apex = 0
    best_apex_config = None
    for v_x in range(v_x_min, v_x_max):
        for v_y in range(v_y_min, v_y_max):
            config = [0, v_x, 0, v_y]
            found_search, apex = run_sim(config, search_border)
            if apex > best_apex and found_search:
                best_apex_config = config
                best_apex = apex
    return best_apex, best_apex_config

def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    border_regex = re.compile(r"target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)")
    test_border = [int(i) for i in border_regex.match(TEST_DATA[0]).groups()]
    with open(INPUT_PATH, 'r') as a_file:
        line = next(a_file)
    input_border = [int(i) for i in border_regex.match(line).groups()]

    test_configs = [
        [0, 7, 0, 2],
        [0, 6, 0, 3],
        [0, 9, 0, 0],
        [0, 17, 0, -4],
        [0, 6, 0, 9],
    ]
    for config in test_configs:
        found_search, apex = run_sim(config, test_border)
        print(f"Config: {config}, found search area {found_search}, apex = {apex}")

    # Now search for velocity config that gives highest height
    # Just do brute force initially
    best_apex, best_apex_config = search_for_apex(0, 150, 0, 150, test_border)
    print(f"Test: Best apex config: {best_apex_config} with apex {best_apex}")

    best_apex, best_apex_config = search_for_apex(0, 150, 0, 150, input_border)
    print(f"Input: Best apex config: {best_apex_config} with apex {best_apex}")

    # Part 2: now need to count all configs that end up inside
    number_inside = 0
    for v_x in range(-100, 100):
        for v_y in range(-100, 100):
            config = [0, v_x, 0, v_y]
            found_search, apex = run_sim(config, test_border)
            if found_search:
                number_inside = number_inside + 1
    print(f"Test: Number configs landing inside search area: {number_inside}")

    # Hand optimised: increased the search range until new values dropped off
    number_inside = 0
    # Optimisations: skip lesser velocities if we undershoot, etc
    for v_x in range(0, 800):
        for v_y in range(-300, 800):
            config = [0, v_x, 0, v_y]
            found_search, apex = run_sim(config, input_border)
            if found_search:
                number_inside = number_inside + 1
    print(f"Input: Number configs landing inside search area: {number_inside}")



    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
