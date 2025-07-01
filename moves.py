# moves.py

def generate_moves(board, white_to_move):
    moves = []
    for r in range(6):
        for c in range(5):
            piece = board[r][c]
            if piece == ".":
                continue
            if white_to_move and piece.isupper():
                moves.extend(piece_moves(board, r, c, piece, True))
            if not white_to_move and piece.islower():
                moves.extend(piece_moves(board, r, c, piece, False))
    return moves

def piece_moves(board, r, c, piece, is_white):
    moves = []
    if piece.upper() == "P":
        dr = -1 if is_white else 1
        nr = r + dr
        if 0 <= nr < 6 and board[nr][c] == ".":
            moves.append(((r, c), (nr, c)))
        for dc in [-1, 1]:
            nc = c + dc
            if 0 <= nr < 6 and 0 <= nc < 5:
                target = board[nr][nc]
                if target != "." and target.isupper() != is_white:
                    moves.append(((r, c), (nr, nc)))
    elif piece.upper() == "R":
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            for i in range(1, 6):
                nr, nc = r + dr*i, c + dc*i
                if not (0 <= nr < 6 and 0 <= nc < 5):
                    break
                target = board[nr][nc]
                if target == ".":
                    moves.append(((r, c), (nr, nc)))
                elif target.isupper() != is_white:
                    moves.append(((r, c), (nr, nc)))
                    break
                else:
                    break
    elif piece.upper() == "N":
        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 6 and 0 <= nc < 5:
                target = board[nr][nc]
                if target == "." or target.isupper() != is_white:
                    moves.append(((r, c), (nr, nc)))
    elif piece.upper() == "K":
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < 6 and 0 <= nc < 5:
                    target = board[nr][nc]
                    if target == "." or target.isupper() != is_white:
                        moves.append(((r, c), (nr, nc)))
    return moves

def apply_move(board, move):
    (from_r, from_c), (to_r, to_c) = move
    piece = board[from_r][from_c]
    new_board = [row.copy() for row in board]
    new_board[to_r][to_c] = piece
    new_board[from_r][from_c] = "."
    # Pawn promotion
    if piece == "P" and to_r == 0:
        new_board[to_r][to_c] = "N"
    elif piece == "p" and to_r == 5:
        new_board[to_r][to_c] = "n"
    return new_board
