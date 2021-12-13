import numpy as np
import re

def eval_board(board, ranges, turn_to_nr):
    win_turns = []
    for r in ranges:
        win_turns.append(max(board[x] for x in r))
    winning_turn = min(win_turns)
    sum_unmarked = sum(turn_to_nr[x] for x in board if x > winning_turn)
    return winning_turn, sum_unmarked * turn_to_nr[winning_turn]

def first_winning(boards, ranges, turn_to_nr):
    first_winning_turn = 1e9
    best_score = 0
    for winning_turn, score in [eval_board(board, ranges, turn_to_nr) for board in boards]:
        if winning_turn < first_winning_turn:
            first_winning_turn = winning_turn
            best_score = score
    print('Score of first winning board:', best_score)

def last_winning(boards, ranges, turn_to_nr):
    first_winning_turn = -1
    best_score = 0
    for winning_turn, score in [eval_board(board, ranges, turn_to_nr) for board in boards]:
        if winning_turn > first_winning_turn:
            first_winning_turn = winning_turn
            best_score = score
    print('Score of last winning board:', best_score)

with open('4_input.txt') as f:
    lines = f.readlines()
    turn_to_nr = np.asarray(lines[0].strip().split(','), np.int64)
    nr_to_turn = { nr: turn for turn, nr in enumerate(turn_to_nr)}
    boards = []
    for i in range(2, len(lines), 6):
        board = []
        for j in range(i, i + 5):
            board.extend(re.split('[ ]+', lines[j].strip()))
        int_board = np.asarray(board, np.int64)
        boards.append([nr_to_turn[int(x)] for x in board])
    ranges = []
    for i in range(5):
        ranges.append(range(5*i, 5*i + 5, 1))
        ranges.append(range(i, i + 25, 5))
    first_winning(boards, ranges, turn_to_nr)
    last_winning(boards, ranges, turn_to_nr)
