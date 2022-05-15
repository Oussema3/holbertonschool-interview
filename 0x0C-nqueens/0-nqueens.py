#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
A program that solves the N queens problem.
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if not isinstance(int(sys.argv[1]), int):
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)


n = int(sys.argv[1])


def solveNQueens(n):
    """ program that solves the N queens problem """
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


def is_valid_state(state, n):
    """ check if it is a valid solution """
    return len(state) == n


def get_candidates(state, n):
    """
    find the next position in the state to populate
    prune down candidates that place the queen into attacks
    """
    if not state:
        return range(n)
    position = len(state)
    candidates = set(range(n))
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    """ search for a safe place to the queens """
    if is_valid_state(state, n):
        state_string = state_to_coor(state)
        solutions.append(state_string)
        return
    candidates = get_candidates(state, n)
    for candidate in candidates:
        state.append(candidate)
        search(state, solutions, n)
        state.remove(candidate)


def state_to_coor(state):
    """ create the required format for output"""
    ret = []
    for x, y in enumerate(state):
        ret.append([x, y])
    return ret

for solution in solveNQueens(n):
    print(solution)
