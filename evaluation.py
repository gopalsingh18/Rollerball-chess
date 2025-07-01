# evaluation.py

def evaluate(board):
    piece_values = {
        "P": 1, "N": 3, "R": 5, "K": 1000,
        "p": -1, "n": -3, "r": -5, "k": -1000
    }
    score = 0
    for row in board:
        for cell in row:
            score += piece_values.get(cell, 0)
    return score
