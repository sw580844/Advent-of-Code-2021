"""
SW 2021-12-05 Advent of code day 4

https://adventofcode.com/2021/day/4
"""

import os
import sys
import re
import pprint
import copy

import numpy as np



INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7",
]

def read_data(lines):
    """
    
    """
    draw = [int(i) for i in lines[0].split(',')]
    boards = []
    this_board = []
    for line in lines[2:]:
        if line == "":
            boards.append(this_board)
            this_board = []
            continue

        # values = [int(i) for i in re.split(r"\s+", line)]
        values = [
            line[0:2],
            line[3:5],
            line[6:8],
            line[9:11],
            line[12:15]
        ]
        values = [int(i) for i in values]
        
        this_board.append(values)
    if len(this_board) > 0:
        boards.append(this_board)

    return draw, boards

def score_board(board, draw):
    """
    
    """
    result = 0
    for row in board:
        for ele in row:
            if ele not in draw:
                result = result + ele
    result = result * draw[-1]
    return result

def check_board(board, draw):
    """
    Checks if draw is all in a row in board
    """
    # Check by row first
    
    for i in range(0, len(board)):
        this_row = board[i]
        
        all_present = True
        for ele in this_row:
            if ele not in draw:
                all_present = False
        if all_present:
            print("All present")
            return True

    # Check by col
    for j in range(0, len(board[0])):
        this_col = [row[j] for row in board]
        all_present = True
        for ele in this_col:
            if ele not in draw:
                all_present = False
        if all_present:
            print("All present")
            return True
    
    return None

def main():
    """
    
    """

    
    
    test_draw, test_boards = read_data(TEST_DATA)
    print("Test draw: {}".format(test_draw))
    print("Test board 0: {},\ntest board -1 {}".format(test_boards[0], test_boards[-1]))
    found_winner = False
    winner_board = None
    winner_draw = None
    for i in range(0, len(test_draw)-5):
        this_draw = test_draw[0:5+i]

        
        for board in test_boards:
            result = check_board(board, this_draw)
            if result:
                print("Found winner with draw {}, board:".format(this_draw))
                pprint.pprint(board)
                found_winner = True
                winner_board = board
                winner_draw = this_draw
            if found_winner:
                break
        if found_winner:
                break
    print(f"Test data score {score_board(winner_board, winner_draw)}")

    # Run on input
    with open(INPUT_PATH, 'r') as a_file:
        lines = [i.rstrip('\n') for i in a_file]
    input_draw, input_boards = read_data(lines)
    print("Length of boards", len(input_boards))

    found_winner = False
    winner_board = None
    winner_draw = None
    for i in range(0, len(input_draw)-5):
        this_draw = input_draw[0:5+i]

        
        for board in input_boards:
            result = check_board(board, this_draw)
            if result:
                print("Found winner with draw {}, board:".format(this_draw))
                pprint.pprint(board)
                found_winner = True
                winner_board = board
                winner_draw = this_draw
            if found_winner:
                break
        if found_winner:
                break
    print(f"Input data score {score_board(winner_board, winner_draw)}")

    # Part 2: find the last winning board
    print("Part 2:")

    found_winner = False
    winner_board = None
    winner_draw = None

    boards_yet_to_clear = copy.deepcopy(test_boards)
    finished = False
    for i in range(0, len(test_draw)-5):
        this_draw = test_draw[0:5+i]

        
        for i, board in enumerate(boards_yet_to_clear):
            result = check_board(board, this_draw)
            if result:
                print("Found winner with draw {}, board:".format(this_draw))
                pprint.pprint(board)
                
                if len(boards_yet_to_clear) == 1:
                    finished = True
                    winner_draw = this_draw
                    winner_board = board
                    break
                boards_yet_to_clear.pop(i)
            if finished:
                break
        if finished:
                break
            
    print(f"Test data score {score_board(winner_board, winner_draw)}")

    found_winner = False
    winner_board = None
    winner_draw = None

    boards_yet_to_clear = copy.deepcopy(input_boards)
    finished = False
    for i in range(0, len(input_draw)-5):
        this_draw = input_draw[0:5+i]

        
        for i, board in enumerate(boards_yet_to_clear):
            result = check_board(board, this_draw)
            if result:
                print("Found winner with draw {}, board:".format(this_draw))
                pprint.pprint(board)
                
                if len(boards_yet_to_clear) == 1:
                    finished = True
                    winner_draw = this_draw
                    winner_board = board
                    break
                boards_yet_to_clear.pop(i)
            if finished:
                break
        if finished:
                break
            
    print(f"Test data score {score_board(winner_board, winner_draw)}")



    sys.exit(0)

if __name__ == "__main__":
    main()