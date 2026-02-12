#!/usr/bin/env python3
"""
Interactive Atomic Chess Game
Play a game of Atomic Chess in the terminal
"""

from ChessVar import ChessVar


def print_welcome():
    """Print welcome message and rules"""
    print("\n" + "="*50)
    print("       WELCOME TO ATOMIC CHESS")
    print("="*50)
    print("\nATOMIC RULES:")
    print("  - Captures trigger explosions (8 surrounding squares)")
    print("  - Capturing piece also explodes!")
    print("  - Pawns are immune to explosions")
    print("  - Win by blowing up opponent's king")
    print("\nHOW TO PLAY:")
    print("  - Enter moves in algebraic notation (e.g., 'e2 e4')")
    print("  - Type 'quit' to exit")
    print("  - Type 'help' for rules reminder")
    print("="*50 + "\n")


def print_help():
    """Print help information"""
    print("\nQUICK REFERENCE:")
    print("  - Columns: a-h (left to right)")
    print("  - Rows: 1-8 (bottom to top)")
    print("  - White pieces: UPPERCASE (P, N, B, R, Q, K)")
    print("  - Black pieces: lowercase (p, n, b, r, q, k)")
    print("  - Empty squares: .")
    print("\nEXAMPLE MOVES:")
    print("  'e2 e4' - Move piece from e2 to e4")
    print("  'd2 d4' - Move piece from d2 to d4")
    print()


def print_board_with_labels(game):
    """Print board with row and column labels"""
    print("\n    a b c d e f g h")
    print("  +-----------------+")

    for i, row in enumerate(game._board):
        row_num = 8 - i
        print(f"{row_num} | {' '.join(row)} | {row_num}")

    print("  +-----------------+")
    print("    a b c d e f g h\n")


def get_move():
    """Get move input from user"""
    while True:
        move = input("Enter move (e.g., 'e2 e4') or 'quit': ").strip().lower()

        if move == 'quit':
            return None

        if move == 'help':
            print_help()
            continue

        # Parse move
        parts = move.split()
        if len(parts) != 2:
            print("Invalid format. Use: 'from_square to_square' (e.g., 'e2 e4')")
            continue

        start, end = parts

        # Basic validation
        if len(start) != 2 or len(end) != 2:
            print("Invalid format. Squares should be 2 characters (e.g., 'e2')")
            continue

        if start[0] not in 'abcdefgh' or end[0] not in 'abcdefgh':
            print("Invalid column. Use letters a-h")
            continue

        if start[1] not in '12345678' or end[1] not in '12345678':
            print("Invalid row. Use numbers 1-8")
            continue

        return start, end


def main():
    """Main game loop"""
    print_welcome()

    game = ChessVar()
    move_count = 0

    while game.get_game_state() == 'UNFINISHED':
        # Display current state
        current_player = "White" if game._current_turn == 'white' else "Black"
        print(f"{'='*50}")
        print(f"Move {move_count + 1} - {current_player}'s turn")
        print_board_with_labels(game)

        # Get move
        move = get_move()

        if move is None:  # User wants to quit
            print("\nThanks for playing! Game ended.")
            return

        start, end = move

        # Try to make the move
        if game.make_move(start, end):
            move_count += 1
            print(f"Move successful: {start} -> {end}")

            # Check for explosions message
            if game._board[game.pos_to_indices(end)[0]][game.pos_to_indices(end)[1]] == '.':
                print("EXPLOSION! Pieces destroyed!")
        else:
            print("Invalid move! Try again.")
            print("   Possible reasons:")
            print("   - Not your piece")
            print("   - Illegal move for that piece")
            print("   - Game already over")

    # Game over
    print("\n" + "="*50)
    print("           GAME OVER!")
    print("="*50)
    print_board_with_labels(game)

    result = game.get_game_state()
    if result == 'WHITE_WON':
        print("WHITE WINS!")
    elif result == 'BLACK_WON':
        print("BLACK WINS!")

    print(f"\nTotal moves: {move_count}")
    print("="*50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please report this issue on GitHub!")
