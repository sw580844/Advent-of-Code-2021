"""
SW 2021-12-18 Advent of code day 18

https://adventofcode.com/2021/day/18
"""

import os
import sys
import datetime

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    [1,2],
    [[1,2],3],
    [9,[8,7]],
    [[1,9],[8,5]],
    [[[[1,2],[3,4]],[[5,6],[7,8]]],9],
    [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]],
    [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]],
]


class SnailfishNumber:
    def __init__(self, value, parent=None):
        self.parent = parent
        if len(value) != 2:
            # Must be a pair
            raise ValueError
        self.value = value
        for i in self.value:
            if isinstance(i, SnailfishNumber):
                i.parent = self

    def __add__(self, other):
        """
        Overload add function
        """
        # Carent a new parent to return
        print(f"other: {other}")
        result = SnailfishNumber([self, other], parent=None)
        print(f"result: {result}")
        # Set parents of children
        self.parent = result
        other.parent = result
        return result

    def __str__(self):
        """
        Overload string function
        """
        return f"[{self.value[0]},{self.value[1]}]"
    # End

def create_snailfish_from_array(this_array):
    """
    
    """
    if isinstance(this_array[0], list):
        left = create_snailfish_from_array(this_array[0])
    else:
        left = this_array[0]
    if isinstance(this_array[1], list):
        left = create_snailfish_from_array(this_array[1])
    else:
        right = this_array[1]

    result = SnailfishNumber([left, right])
    for i in result.value:
        if isinstance(i, SnailfishNumber):
            i.parent = result
    return result

def explode_find(sn, depth=0):
    if not isinstance(sn, SnailfishNumber):
        # Gotten to root integer, not an issue
        return None
    if depth == 4:
        print(f"Explode {sn}")
        return sn
    for child in sn.value:
        # Check left, then check right
        result = explode_find(sn.value[0], depth=depth+1)
        if result is None:
            return explode_find(sn.value[1], depth=depth+1)
        else:
            return result

def explode_check(snailfish_number):
    """
    
    """
    # Recurse through, if at depth 4 we need to explode
    to_explode = explode_find(snailfish_number)
    if to_explode is not None:
        print(f"Found: {to_explode}")
        # Explode left, then right
        old_val = to_explode
        # Left first, ascend until we can go left
        while True:



def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]

    # Testing examples
    n1 = SnailfishNumber([1,2])
    print(f"n1: {n1}")
    n2 = SnailfishNumber([SnailfishNumber([3,4]), 5])
    print(f"n2: {n2}")
    print("n1 + n2: ", n1 + n2)

    #
    print("Creating from array")
    n1 = create_snailfish_from_array([[[[[9,8],1],2],3],4])
    print(n1, type(n1), type(n1.value[0]))
    explode_check(n1)

    

    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
