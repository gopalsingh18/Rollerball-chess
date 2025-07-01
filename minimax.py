# minimax.py

from moves import generate_moves, apply_move
from evaluation import evaluate

def minimax(board, depth, alpha, beta, maximizing):
    # Check if kings are captured
    flat = [cell for row in board for cell in row]
    if "K" not in flat:
        return -9999, None  # Black wins
    if "k" not in flat:
        return 9999, None   # White wins

    if depth == 0:
        return evaluate(board), None

    best_move = None
    moves = generate_moves(board, maximizing)

    if not moves:
        return evaluate(board), None

    if maximizing:
        max_eval = -float("inf")
        for move in moves:
            new_board = apply_move(board, move)
            eval, _ = minimax(new_board, depth-1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for move in moves:
            new_board = apply_move(board, move)
            eval, _ = minimax(new_board, depth-1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
