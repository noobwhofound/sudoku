import solver
from random import randint
from typing import Final
def GENERATE_BOARD(board):
    find = solver.find_empty_cell(board)
    if find is None:
        return True
    else:
        row, col = find
    for number in range(1, 10):
        randomNumber = randint(1, 9)
        if solver.is_valid(board, row, col, randomNumber):
            board[row][col] = randomNumber
            if GENERATE_BOARD(board):
                return True

            board[row][col] = 0
    return False

def DELETE_CELLS(board, number):
    while number :
        row = randint(0, 8)
        col = randint(0, 8)
        if board[row][col] != 0 :
            board[row][col] = 0
            number -= 1

def GENERATE(board, level):
    GENERATE_BOARD(board)
    if level == 10001 :
        DELETE_CELLS(board, 2)
    if level == 0 :
        DELETE_CELLS(board, 20)
    elif level == 1:
        DELETE_CELLS(board, 30)
    elif level == 2 :
        DELETE_CELLS(board, 40)
    elif level == 3:
        DELETE_CELLS(board, 50)
    elif level == 4 :
        DELETE_CELLS(board, 60)

EMPTY_BOARD : Final = [[0 for _ in range(9)] for _ in range(9)]

        
    