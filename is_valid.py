import solver
import copy as c
def IS_VALID(start_board, board, row, col, number):
    copy = c.deepcopy(board)
    copy[row][col] = 0
    if (board[row][col] == 0 or start_board[row][col] == 0) and solver.is_valid(copy, row, col, number):
        return True
    return False
