"""
SW 2021-12-17 Advent of code day 10

https://adventofcode.com/2021/day/10

Could potentially combine the scoring system, but at this stage I'd like to keep it separate
through part 1 and part 2
"""

import os
import sys
import datetime

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]




def get_inverse(this_char):
    """
    Gets corresponding opening or close grouper
    """
    inverse_dict = {
        "{" : "}",
        "[" : "]",
        "<" : ">",
        "(" : ")",
        "}" : "{",
        "]" : "[",
        ">" : "<",
        ")" : "(",
    }
    return inverse_dict[this_char]


def get_line_score(line, verbose=False):
    """
    Gets score a single line
    """
    opening_chars = ["{", "[", "<", "("]
    closing_chars = ["}", "]", ">", ")"]
    score_table = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137,
    }
    opens = []
    for i, this_char in enumerate(line):

        if this_char in opening_chars:
            opens.append(this_char)
        if i == 0:
            continue
        if this_char in closing_chars:
            # This is a closing char, it should close off the last group
            expected = get_inverse(opens[-1])
            if this_char != expected:
                if verbose:
                    print(f"Expected {expected} but got {this_char} at {i}")
                return score_table[this_char]
            else:
                opens.pop(-1)
    # Got to end, no score
    return 0

def get_line_score_2(line, verbose=False):
    """
    Gets score of a single line, but now for part 2
    """
    opening_chars = ["{", "[", "<", "("]
    closing_chars = ["}", "]", ">", ")"]
    score_table = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4,
    }
    opens = []
    for i, this_char in enumerate(line):
        if this_char in opening_chars:
            opens.append(this_char)
        if i == 0:
            continue
        if this_char in closing_chars:
            # This is a closing char, it should close off the last group
            expected = get_inverse(opens[-1])
            if this_char != expected:
                if verbose:
                    print(f"Expected {expected} but got {this_char} at {i}")
                # This line should already by uncorrupted, but this snuck through. Raise valuerror
                raise ValueError
            else:
                opens.pop(-1)
    # Got to end, need to find characters required to complete
    to_close = ""
    for i in opens[::-1]:
        to_close = to_close + get_inverse(i)
    if verbose:
        print(f"String to close: {to_close}")
    result = 0
    for i in to_close:
        result = result * 5 + score_table[i]
    return result

def get_score(lines, verbose=False):
    """
    Gets score of a bunch of lines
    """
    result = 0
    for line in lines:
        result = result + get_line_score(line, verbose)
    return result

def get_score_2(lines, verbose=False):
    """
    Part 2 scoring system

    Score each line, then sort, then take middle value.
    Guaranteed to get odd number of lines
    """
    incomplete_lines = [i for i in lines if get_line_score(i, verbose=verbose) == 0]
    incomplete_scores = [get_line_score_2(i, verbose=verbose) for i in incomplete_lines]
    incomplete_scores = sorted(incomplete_scores)
    return incomplete_scores[len(incomplete_scores) // 2]

def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]

    print("Part 1")
    test_score = get_score(TEST_DATA, True)
    print(f"Test data, score: {test_score}")

    input_score = get_score(input_lines)
    print(f"Input data score: {input_score}")

    print("Part 2:")
    test_subset = [TEST_DATA[i] for i in [0, 1, 3, 6, 9]]
    for line in test_subset:
        print(f"Line: {line}")
        if get_line_score(line) == 0:
            print("Uncorrupted")
            new_score = get_line_score_2(line, verbose=True)
            print(f"New score: {new_score}")
    test_score = get_score_2(TEST_DATA)
    print(f"Score of test data set: {test_score}")

    input_score = get_score_2(input_lines)
    print(f"Score of input data {input_score}")

    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
