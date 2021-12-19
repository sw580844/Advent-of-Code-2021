"""
SW 2021-12-18 Advent of code day 18

https://adventofcode.com/2021/day/18
"""

import os
import sys
import datetime
import re
import collections



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

def add_snailfish_number(n1, n2):
    """
    
    """
    return [n1] + [n2]

class SnailfishNumber:
    def __init__(self, n1, n2):
        """
        
        """
        self.parent = None
        self.left = n1
        self.right = n2

    def __add__(self, other):
        """
        Overload add function
        """
        result = SnailfishNumber(self, other)
        self.parent = result
        self.other = result
        return result

    def __str__(self):
        """
        Overload string function
        """
        return f"[{self.left},{self.right}]"

class SnailfishTree:
    def __init__(self, value, parent):
        """
        
        """
        self.parent = parent
        # Value should be a list of int or more snailfish
        self.value = [value]

    def __add__(self, other):
        """
        Overload add function
        """
        result = SnailfishTree([self.value, other.value], None)
        self.parent = result
        other.parent = result
        return result

    def __str__(self):
        """
        Overload string function
        """
        return f"[{[str(i) for i in self.value]}]"

def create_snailfish_from_array(this_input):
    """
    
    """
    if isinstance(this_input[0], list):
        left = create_snailfish_from_array(this_input[0])
    else:
        left = this_input[0]
    if isinstance(this_input[1], list):
        right = create_snailfish_from_array(this_input[1])
    else:
        right = this_input[1]

    result = SnailfishNumber(left, right)
    if isinstance(result.left, SnailfishNumber):
        result.left.parent = result
    if isinstance(result.right, SnailfishNumber):
        result.right.parent = result

    
    return result


def explode_sn(snailfish_number):
    """
    
    """
    # Need to remove this number, add to leftmost neighbour or rightmost neighbour
    print(f"Exploding {snailfish_number}")
    left_path = find_separate_path(snailfish_number.parent, snailfish_number, -1)
    print(f"left path is {left_path}")
    right_path = find_separate_path(snailfish_number.parent, snailfish_number, 1)
    print(f"right path is {right_path}")

    # Okay, ascend tree until we can go in appropriate direction without backtracking
    last_checked = snailfish_number
    while True:
        if last_checked is None:
            print("No parent")
            break
        elif last_checked.parent.right != last_checked:
            # Okay we can now start descending or doing
            if not isinstance(last_checked.parent.right, SnailfishNumber):
                # Not a snailfish number
        else:
            # Ascend and try again
            last_checked = last_checked.parent
        






    # Add to left, add to right, then set this snailfish pair to zero
    # Need to check if the left path is already at left node
    if left_path is not None:
        if isinstance(left_path, SnailfishNumber):
            add_value(snailfish_number.left, left_path, 1)
        else:
            1
    if right_path is not None:
        if isinstance(right_path, SnailfishNumber):
            add_value(snailfish_number.right, right_path, -1)
        else:
            1
    snailfish_number = 0
    return

def add_value(value, tree, direction):
    """
    Descends in direction, finds first leaf node of tree and adds to it
    """
    print(f"Add value {value} to {tree} with direction {direction}")
    if direction not in [-1, 1]:
        raise ValueError


    if direction == -1:
        if not isinstance(tree.left, SnailfishNumber):
            tree.left = tree.left + value
            return
        else:
            add_value(value, tree.left, direction)
    if direction == 1:
        if not isinstance(tree.right, SnailfishNumber):
            tree.right = tree.right + value
            return 
        else:
            add_value(value, tree.right, direction)
    # End of func

def find_separate_path(tree, previous, direction):
    """
    # Ascend tree until we can go direction without backtracking
    """
    if direction not in [-1, 1]:
        raise ValueError
    if direction == -1:
        if tree.left == previous:
            # Ascend again
            if tree.parent is None:
                return None
            else:
                return find_separate_path(tree.parent, tree, direction)
        else:
            return tree.left
    if direction == 1:
        if tree.right == previous:
            # Ascend again
            if tree.parent is None:
                return None
            else:
                return find_separate_path(tree.parent, tree, direction)
        else:
            return tree.right
    # End



def explode_check(snailfish_number, depth=0):
    """
    
    """
    if depth == 4:
        print(f"Explode {snailfish_number}")
        explode_sn(snailfish_number)
        return True
    if not isinstance(snailfish_number, SnailfishNumber):
        return False
    for child in [snailfish_number.left, snailfish_number.right]:
        if isinstance(child, SnailfishNumber):
            explode_check(child, depth=depth+1)
        else:
            1
    return False




def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    with open(INPUT_PATH, 'r') as a_file:
        input_lines = [i.rstrip("\n") for i in a_file]

    # Testing examples
    # n1 = SnailfishTree(1,2)
    # n2 = SnailfishTree(SnailfishTree(3,4), 5)
    # print(n1 + n2)

    n1 = create_snailfish_from_array([[[[[9,8],1],2],3],4])
    print(n1, type(n1), type(n1.left))
    explode_check(n1)
    print(f"After explode check: {n1}")
    # n1 = create_snailfish_from_array([7,[6,[5,[4,[3,2]]]]])
    # print(n1, type(n1), type(n1.left))
    # explode_check(n1)

    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
