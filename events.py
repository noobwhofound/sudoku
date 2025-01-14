import solver
import generate
from is_valid import IS_VALID
import copy as c
def DEAD_END(board):
    copy = c.deepcopy(board)
    if not solver.solve_sudoku(copy):
        return True
    return False

def NEW_BOARD(board, diff):
    board = generate.EMPTY_BOARD
    copy = c.deepcopy(board)
    generate.GENERATE(copy, diff)
    return copy

def WON(start_board, board):
    copy = c.deepcopy(start_board)
    if solver.solve_sudoku(copy):
        if copy == board :
            return True
    return False

def MOVE(start_board, board, row, col, number):
    if not IS_VALID(start_board, board, row - 1, col - 1, number):
        return None
    board[row - 1][col - 1] = number
    return True

