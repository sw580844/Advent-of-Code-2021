"""
SW 2021-12-08 Advent of code day 12

https://adventofcode.com/2021/day/12

NOTE: the performance here is pretty bad, needs to be tuned up
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
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

TEST_DATA_2 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]

def parse_data(lines):
    """
    
    """
    neighbour_map = {}
    for line in lines:
        pt1, pt2 = line.split("-")
        if pt1 not in neighbour_map:
            neighbour_map[pt1] = []
        if pt2 not in neighbour_map:
            neighbour_map[pt2] = []
        if pt1 not in neighbour_map[pt2]:
            neighbour_map[pt2].append(pt1)
        if pt2 not in neighbour_map[pt1]:
            neighbour_map[pt1].append(pt2)

    return neighbour_map

def generate_paths(neighbour_map, max_depth=100):
    """
    
    """
    complete_paths = []
    path_candidates = [["start",],]
    counter = 0
    while True:
        # While we have path candidates, those not yet finished or stuck, try to go another step
        new_path_candidates = []
        for this_candidate in path_candidates:
            last_spot = this_candidate[-1]
            these_neighbours = neighbour_map[last_spot]
            # Filter out neighbours that are lower case and visited before
            # Could turn into map or list comprehension
            filtered_neighbours = []
            for neighbour in these_neighbours:
                is_lowercase = (neighbour == neighbour.lower())
                already_visited = neighbour in this_candidate
                if already_visited and is_lowercase:
                    continue
                else:
                    filtered_neighbours.append(neighbour)
            these_new_candidates = [this_candidate + [neighbour] for neighbour in filtered_neighbours]
            complete_paths = complete_paths + [i for i in these_new_candidates if i[-1] == "end"]
            ongoing_paths = [i for i in these_new_candidates if i[-1] != "end"]
            new_path_candidates = new_path_candidates + ongoing_paths

        path_candidates = new_path_candidates
        counter = counter + 1
        if counter > max_depth:
            print(f"Breaking, max depth recahed")
            break
        # If no more paths to work on, break out
        if len(path_candidates) == 0:
            break

    return complete_paths

def generate_paths_2(neighbour_map, max_depth=100):
    """
    For part 2, now we can enter a single small cave twice and the rest once
    """
    complete_paths = []
    path_candidates = [["start",],]
    counter = 0
    while True:
        # While we have path candidates, those not yet finished or stuck, try to go another step
        new_path_candidates = []
        for this_candidate in path_candidates:
            last_spot = this_candidate[-1]
            these_neighbours = neighbour_map[last_spot]
            # Filter out neighbours that are lower case and visited before
            # Could turn into map or list comprehension
            filtered_neighbours = []
            for neighbour in these_neighbours:
                if neighbour == neighbour.upper():
                    filtered_neighbours.append(neighbour)
                    continue
                if neighbour == "start":
                    continue
                
                already_visited = neighbour in this_candidate
                # check if a small cave has already been double visited
                small_caves_visited = [i for i in this_candidate if i.lower() == i and i not in ["start", "end"]]
                # print(f"small caves visisted: {small_caves_visited}")
                double_visited = False
                for name in small_caves_visited:
                    if len([i for i in small_caves_visited if i == name]) > 1:
                        double_visited = True
                        break

                if (already_visited and double_visited):
                    continue
                else:
                    filtered_neighbours.append(neighbour)
            these_new_candidates = [this_candidate + [neighbour] for neighbour in filtered_neighbours]
            complete_paths = complete_paths + [i for i in these_new_candidates if i[-1] == "end"]
            ongoing_paths = [i for i in these_new_candidates if i[-1] != "end"]
            new_path_candidates = new_path_candidates + ongoing_paths
        path_candidates = new_path_candidates
        print(len(path_candidates), len(complete_paths))
        # print(path_candidates)
        counter = counter + 1
        if counter > max_depth:
            print(f"Breaking, max depth recahed")
            break
        # If no more paths to work on, break out
        if len(path_candidates) == 0:
            break

    return complete_paths

def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")
    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]

    # Input is a list of nodes and how they connect
    test_neighbour_map = parse_data(TEST_DATA)
    print(f"Test data neighbour map: {test_neighbour_map}")
    # # Need to find number of paths from start to end that only cross lower case nodes once
    # complete_paths = generate_paths(test_neighbour_map)
    # print("Test data, complete paths:")
    # for i in complete_paths:
    #     print(i)
    # print(f"Test data, Total number of paths: {len(complete_paths)}")

    # test_neighbour_map_2 = parse_data(TEST_DATA_2)
    # print(f"Test data 2 neighbour map: {test_neighbour_map_2}")
    # # Need to find number of paths from start to end that only cross lower case nodes once
    # complete_paths = generate_paths(test_neighbour_map_2)
    # print("Test data 2, complete paths:")
    # for i in complete_paths:
    #     print(i)
    # print(f"Test data 2, Total number of paths: {len(complete_paths)}")

    # input_neighbour_map = parse_data(input_lines)
    # print(f"Input data neighbour map: {input_neighbour_map}")
    # complete_paths = generate_paths(input_neighbour_map)
    # print("Input data, complete paths:")
    # for i in complete_paths:
    #     print(i)
    # print(f"Input data, Total number of paths: {len(complete_paths)}")

    # Part 2
    print("Part 2:")
    complete_paths = generate_paths_2(test_neighbour_map, max_depth=20)
    print("Test data, complete paths:")
    for i in complete_paths:
        print(i)
    print(f"Test data, Total number of paths: {len(complete_paths)}")

    test_neighbour_map_2 = parse_data(TEST_DATA_2)
    print(f"Test data 2 neighbour map: {test_neighbour_map_2}")
    # Need to find number of paths from start to end that only cross lower case nodes once
    complete_paths = generate_paths_2(test_neighbour_map_2)
    print(f"Test data 2, Total number of paths: {len(complete_paths)}")

    input_neighbour_map = parse_data(input_lines)
    print(f"Input data neighbour map: {input_neighbour_map}")
    complete_paths = generate_paths_2(input_neighbour_map, max_depth=25)
    print(f"Input data, Total number of paths: {len(complete_paths)}")
    for i in complete_paths:
        if len(i) > 9:
            print(i)
    print(f"Input data, Total number of paths: {len(complete_paths)}")
    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}, duration {time_end - time_start}")




    sys.exit(0)

if __name__ == "__main__":
    main()