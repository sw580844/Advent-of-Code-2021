"""
SW 2021-12-08 Advent of code day 8

https://adventofcode.com/2021/day/8
"""

import os
import sys

import numpy as np



INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

def part_1(data):
    """
    Part 1: Count how many times the the 1,4,7,8 digits appear
    (ie. how many times there are groups of 2,4,3,7 on the right of |)
    """
    result = 0
    for line in data:
        line_input, line_output = line.split("|")
        output_segment_groups = [i for i in line_output.split(" ") if i != ""]
        result = result + len([i for i in output_segment_groups if len(i) in [2,4,3,7]])
    return result

def part_2(data):
    """
    Now we need to decode the keys
    """
    
    # Idea: create (7,7) matrix to link candidates
    # Start with ones, because without any info any of them could be any of them
    # Apparently the stuff on the left does include every value
    result = np.ones((7,7))
    digit_codes = ["a", "b", "c", "d", "e", "f", "g"]
    for line in data:
        segment_groups = line.replace(" | ", " ").split(" ")
        # Go through by elimination 
        # First step, if there's a two segment group, link to (c,f)
        segment = [i for i in segment_groups if len(i) == 2]
        idxs = [digit_codes.index(i) for i in segment[0]]
        
        
        # Go through the row, turn off certain element
        mask = np.zeros_like(result[0])
        for idx in idxs:
            mask[idx] = 1
        result[digit_codes.index("c"), :] = result[digit_codes.index("c"), :] * mask
        result[digit_codes.index("f"), :] = result[digit_codes.index("f"), :] * mask
        
        # Next one, the three segment code refers to digit 7, acf
        segment = [i for i in segment_groups if len(i) == 3]
        idxs = [digit_codes.index(i) for i in segment[0]]
        mask = np.zeros_like(result[0])
        for idx in idxs:
            mask[idx] = 1
        result[digit_codes.index("a"), :] = result[digit_codes.index("a"), :] * mask
        result[digit_codes.index("c"), :] = result[digit_codes.index("c"), :] * mask
        result[digit_codes.index("f"), :] = result[digit_codes.index("f"), :] * mask
        print(result)

        # Next, the four segments that refer to digit 4, bcdf
        segment = [i for i in segment_groups if len(i) == 4]
        idxs = [digit_codes.index(i) for i in segment[0]]
        mask = np.zeros_like(result[0])
        for idx in idxs:
            mask[idx] = 1
        result[digit_codes.index("b"), :] = result[digit_codes.index("b"), :] * mask
        result[digit_codes.index("c"), :] = result[digit_codes.index("c"), :] * mask
        result[digit_codes.index("d"), :] = result[digit_codes.index("d"), :] * mask
        result[digit_codes.index("f"), :] = result[digit_codes.index("f"), :] * mask
        print(result)

        # Next we need to do the degenerate states, with 5 idxs
        segment = [i for i in segment_groups if len(i) == 5]
        print(segment)



        
        


        break
        
        


def main():
    """
    Main entry point
    """

    
    test_lines = TEST_DATA
    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]
    
    print("Part 1:")
    test_result = part_1(test_lines)
    print(f"Part 1, test data: number of times the digits 1,4,7,8 are attempting to appear: {test_result}")
    input_result = part_1(input_lines)
    print(f"Part 1, input data: number of times the digits 1,4,7,8 are attempting to appear: {input_result}")

    # Part 2
    part_2(test_lines)

    sys.exit(0)

if __name__ == "__main__":
    main()