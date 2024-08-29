# Author: Jomel Bautista
# GitHub username: jogarbaut
# Date: 2024/06/09
# Description: Portfolio project of an implementation of a chess variant, Atomic Chess.

class ChessVar:
    """ Represents a ChessVar implementation with methods based on atomic chess"""
    def __init__(self):
        """ Initialize data members"""
        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self._current_turn = 'white'
        self._game_state = 'UNFINISHED'

    def get_game_state(self):
        """ Returns game state """
        return self._game_state

    def is_valid_move(self, start, end):
        """
        Method to validate the move being entered
        Parameters: start position; end position
        Returns: True or False
        """
        start_row, start_col = start
        end_row, end_col = end
        piece = self._board[start_row][start_col]
        target = self._board[end_row][end_col]

        # Check piece belongs to the player making the move
        if (piece.isupper() and self._current_turn != 'white') or (piece.islower() and self._current_turn != 'black'):
            return False

        # Calculate the change in row and col based on parameters
        change_in_row = end_row - start_row
        change_in_col = end_col - start_col

        # Validation of move for Pawn
        if piece.lower() == 'p':
            # Determine valid direction by checking if white or black
            direction = -1 if piece.isupper() else 1

            # Moving forward by one square and check correct direction and target slot is empty
            if change_in_col == 0 and change_in_row == direction and target == '.':
                return True

            # Check if the pawn is in its initial position
            start_row_check = 6 if piece.isupper() else 1

            # Moving forward by two squares and on first move of player
            if change_in_col == 0 and change_in_row == 2 * direction and start_row == start_row_check and target == '.':
                return True

            # Capturing for pawn
            if abs(change_in_col) == 1 and change_in_row == direction and target != '.':
                return True

        # Validation of move for rook
        elif piece.lower() == 'r':
            # Check that the rook is moving in a straight line
            if change_in_row == 0 or change_in_col == 0:
                return True

        # Validation for knight
        elif piece.lower() == 'n':
            # Check path of knight follows required path
            if abs(change_in_row) == 2 and abs(change_in_col) == 1 or (abs(change_in_row) == 1 and abs(change_in_col) == 2):
                return True

        # Validation for bishop
        elif piece.lower() == 'b':
            # Check path of knight follows required path
            if abs(change_in_row) == abs(change_in_col):
                return True

        # Validation for queen
        elif piece.lower() == 'q':
            if change_in_row == 0 or change_in_col == 0 or abs(change_in_row) == abs(change_in_col):
                return True

        # Validation for king
        elif piece.lower() == 'k':
            if abs(change_in_row) <= 1 and abs(change_in_col) <= 1:
                return True

        # Catch case that does not match any of the piece types
        return False

    def make_move(self, start_pos, end_pos):
        """
        Method to execute a move entered by the player
        Parameters: start position; end position
        Returns: True or False (True if the move was successfully executed)
        """

        # Check that the game is not unfinished
        if self._game_state != 'UNFINISHED':
            return False

        # Determine the position on the board based by converting to index values
        start_row, start_col = self.pos_to_indices(start_pos)
        end_row, end_col = self.pos_to_indices(end_pos)

        # Determine the piece type based on the position on the board
        piece = self._board[start_row][start_col]

        # Check if the starting position is at an empty slot, if no piece, return False
        if piece == '.':
            return False

        # Check if the move is valid
        if not self.is_valid_move((start_row, start_col), (end_row, end_col)):
            return False

        # Move piece and handle atomic capture
        self._board[start_row][start_col] = '.'  # Replace start slot with an empty marker

        if self._board[end_row][end_col] != '.':
            if self._board[end_row][end_col].lower() == 'k' and piece.lower() == 'k':
                return False  # Prevent both kings from being blown up at same time
            self.explode((end_row, end_col))
            self._board[end_row][end_col] = '.'  # Remove piece that caused explosion
        else:
            # If there was an empty slot at the end position, only move piece
            self._board[end_row][end_col] = piece

        # Check if game is over
        if not self.kings_both_exist():
            if self._current_turn == 'white':
                self._game_state = 'WHITE_WON'
            else:
                self._game_state = 'BLACK_WON'
            return True

        # Switch turns
        if self._current_turn == 'white':
            self._current_turn = 'black'
        else:
            self._current_turn = 'white'

        return True

    def pos_to_indices(self, pos):
        """ Method to determine the index to identify location on board"""
        col_letters = 'abcdefgh'
        col = col_letters.index(pos[0])
        row = 8 - int(pos[1])
        return row, col

    def kings_both_exist(self):
        # Method to check if kings still exist to help determine if the game is over
        white_king = False
        black_king = False
        for row in self._board:
            for piece in row:
                if piece == 'K':
                    white_king = True
                if piece == 'k':
                    black_king = True
        return white_king and black_king

    def explode(self, pos):
        # Method for atomic explosion - 8 squares immediately surrounding the captured piece in all the directions
        row, col = pos
        for row in range(row - 1, row + 2):
            for col in range(col - 1, col + 2):
                # Change all exploded squares to empty unless it is a pawn
                if 0 <= row < 8 and 0 <= col < 8 and self._board[row][col].lower() != 'p':
                    self._board[row][col] = '.'

    def print_board(self):
        # Method for printing board
        for row in self._board:
            print(' '.join(row))
        print()

