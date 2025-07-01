# main.py

from board import initial_board, print_board
from minimax import minimax
from moves import generate_moves, apply_move

def main():
    board = initial_board()
    white_to_move = True

    while True:
        print_board(board)

        # Check if kings are captured
        flat = [cell for row in board for cell in row]
        if "k" not in flat:
            print("White wins!")
            break
        if "K" not in flat:
            print("Black wins!")
            break

        if white_to_move:
            legal_moves = generate_moves(board, white_to_move)

            def move_to_str(move):
                (fr, fc), (tr, tc) = move
                return f"{chr(fc + ord('a'))}{6 - fr}{chr(tc + ord('a'))}{6 - tr}"

            legal_move_strs = [move_to_str(m) for m in legal_moves]

            while True:
                move_str = input("Enter your move (e.g., a2a3): ").strip()
                if move_str in legal_move_strs:
                    idx = legal_move_strs.index(move_str)
                    move = legal_moves[idx]
                    break
                else:
                    print("Invalid move! Please enter a legal move.")
            
            board = apply_move(board, move)

        else:
            print("AI thinking...")
            _, best_move = minimax(board, depth=3, alpha=-float("inf"), beta=float("inf"), maximizing=False)
            if best_move is None:
                print("AI resigns!")
                break
            board = apply_move(board, best_move)

        white_to_move = not white_to_move

if __name__ == "__main__":
    main()
