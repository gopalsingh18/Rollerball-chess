# board.py

def initial_board():
    return [
        ["r", "n", "k", "n", "r"],
        ["p", "p", "p", "p", "p"],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P"],
        ["R", "N", "K", "N", "R"]
    ]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
