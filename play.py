from events import *
from solver import *
import os
import copy as c

while True:
    oooo = input("press any key to continue..")

    diff = input("choose difficulty : baby, easy, medium, hard, insane : ")
    if diff == 'devmode':
        diff = 10001
    if diff == 'baby' :
        diff = 0
    elif diff == 'easy':
        diff = 1
    elif diff == 'medium':
        diff == 2
    elif diff == 'hard':
        diff = 3
    elif diff == 'insane':
        diff = 4
    else :
        diff = 4
    
    board = None
    board = NEW_BOARD(board, diff)
    start_board = c.deepcopy(board)

    f = False
    r = False
    w = False
    while True :
        os.system('cls')
        if r:
            board = c.deepcopy(start_board)
            r = False
        if f:
            print("not a valid move, try again")
            f = False
        print("\n\n\n\n\n")
        solver.print_board(board)
        if w:
            w = False
            break
        move = input()
        if move.lower() == 'clear':
            r = True
            continue
        elif move.lower() == 'new':
            break
        row, col, number = move.split(" ")
        if not (MOVE(start_board, board, int(row), int(col), int(number))):
            f == True
        
        if DEAD_END(board):
            awns = input("it seems like you are not gonna succes so want to reset ? y / n   ")  
            if awns.lower() == 'y' : 
                r = True
                continue
            else :
                print("ok, good luck with winning")

        if WON(start_board, board):
            print("congrats, you won!!!")
            w = True