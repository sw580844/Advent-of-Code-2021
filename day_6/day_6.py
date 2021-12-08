"""
SW 2021-12-05 Advent of code day 6

https://adventofcode.com/2021/day/6
"""

import os
import sys
import copy




INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "3,4,3,1,2"
]

def update_state(state):
    """
    Takes a list of ints representing fish state, updates by a day
    """

    new_state = []
    new_fish = []
    for fish in state:
        if fish == 0:
            fish = 6
            new_fish.append(8)
        else:
            fish = fish - 1
        new_state.append(fish)
    new_state = new_state + new_fish
    return new_state

def create_state_dict(state):
    """
    Returns a state dict from list of fish and their spawn times
    """
    MAX_SPAWN_TIME = 8
    result = dict([(i, 0) for i in range(0, MAX_SPAWN_TIME+1)])

    for spawn_time in state:
        result[spawn_time] = result[spawn_time] + 1
    return result

def update_state_2(state_dict):
    """
    Motivated by part 2, when we realise we can't keep a list of fish ages

    Args:
        state_dict - Dict of fish ages
    """
    
    # Update the fish about to give spawned
    result = copy.deepcopy(state_dict)
    new_fish = result[0]
    for i in range(0, 8):
        result[i] = result[i+1]
    result[8] = new_fish # New fish spawned
    result[6] = result[6] + new_fish # Reset the timer on the fish that just spawned
    return result

def main():
    """
    Main entry point
    """

    test_state = [int(i) for i in TEST_DATA[0].split(",")]
    with open(INPUT_PATH, 'r', encoding="utf-8") as a_file:
        input_state = [int(i) for i in next(a_file).split(",")]

    print("Part 1:")
    current_state = test_state
    print(f"Test data, start: {current_state}")
    for i in range(1, 19):
        current_state = update_state(current_state)
        print(f"Day {i}, state {current_state}")
    print(f"Test data: at end of run, {len(current_state)} fish")

    # Run with input data
    current_state = input_state
    for i in range(1, 81):
        current_state = update_state(current_state)
    print(f"Input data: at end of run, {len(current_state)} fish")

    # Part 2: Now it gets silly
    print("Part 2:")
    state_dict = create_state_dict(test_state)
    for i in range(1, 256+1):
        print(f"i: {i}, fish {sum(state_dict.values())}")
        state_dict = update_state_2(state_dict)
    print(f"Test data: at end of run, {sum(state_dict.values())} fish")

    state_dict = create_state_dict(input_state)
    for i in range(1, 256+1):
        print(f"i: {i}, fish {sum(state_dict.values())}")
        state_dict = update_state_2(state_dict)
    print(f"Input data: at end of run, {sum(state_dict.values())} fish")


    sys.exit(0)

if __name__ == "__main__":
    main()