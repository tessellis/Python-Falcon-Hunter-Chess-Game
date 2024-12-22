# Author: Tess Ellis
# GitHub username: tessellis
# Date: 03/17/24
# Description: A program that simulates Falcon-Hunter Chess, an abstract board game that is a variant of chess.

"""
Visual representation of my 8 by 8 board using upper-case for White and lower-case for Black:
  a b c d e f g h
 +-----------------+
8| r n b q k b n r |  hf
7| p p p p p p p p |
6|                 |
5|                 |
4|                 |
3|                 |
2| P P P P P P P P |
1| R N B Q K B N R |   HF
 +-----------------+
  a b c d e f g h

Note: H = White's Hunter (off board)
      F = White's Falcon (off board)
      h = Black's Hunter (off board)
      F = Black's Falcon (off board)
"""


class ChessVar:
    # SCENARIO 1: Keeping track of the current board position
    def __init__(self):
        """
        Since the ChessVar init method should initialize all data members, I still need to add more to this section
        """
        self._game_state = 'UNFINISHED'  # Initialize the game state to 'UNFINISHED' when it begins
        # SCENARIO 2: Keeping track of turn order (see make_move function also)
        self._turn = 'WHITE'  # White always has the first turn
        self._fairy_pieces = ['F', 'H', 'f', 'h']  # Each player gets one falcon and one hunter piece (not in play yet)

        # Keeping track of the current board position
        """
        Below, upper-case letters represent White's pieces, and lower-case letters represent Black's pieces. I'm
        thinking about using dictionaries (rather than lists) because it may end up being easier to "reference" or
        find piece positions using dictionary syntax.
        """
        self._board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],  # black pieces
            ["p"] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["P"] * 8,
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # white pieces
        ]

    def display_board(self):
        print("    a b c d e f g h")
        print("")
        row_number = 8
        for row in self._board:
            print(row_number, "|", ' '.join(row), "|")
            row_number -= 1
        print("")

    def make_move(self, prev_pos, new_pos):
        if self._game_state != 'UNFINISHED':
            return False

        prev_pos_mapped_row, prev_pos_mapped_col = self.mapping_function(prev_pos)
        piece = self.get_piece_at_position(prev_pos_mapped_row, prev_pos_mapped_col)
        # print(piece)

        # checking if it's the correct player's turn:
        if piece.isupper():  # it is a white piece
            if self._turn != 'WHITE':
                return False  # all good
        elif piece.islower():  # it is a black piece
            if self._turn != 'BLACK':
                return False  # all good

        new_pos_mapped_row, new_pos_mapped_col = self.mapping_function(new_pos)

        if not self.check_move_validity(piece, prev_pos_mapped_row, new_pos_mapped_row, prev_pos_mapped_col,
                                        new_pos_mapped_col):
            # print("Invalid move")
            return False

        # after we know that it is a valid move, we just update the new position to have our piece, and the old position
        # to now be empty
        piece_at_new_position = self._board[new_pos_mapped_row][new_pos_mapped_col]
        self._board[new_pos_mapped_row][new_pos_mapped_col] = piece  # Move piece to new position
        self._board[prev_pos_mapped_row][prev_pos_mapped_col] = ' '  # Update previous position to empty

        if self._game_state == "WHITE_WON":
            print("Congrats! White has one the game!")
        elif self._game_state == "BLACK_WON":
            print("Congrats! Black has one the game!")
        else:
            if self._turn == 'WHITE':
                self._turn = 'BLACK'
            else:
                self._turn = 'WHITE'
        return True

    def enter_fairy_piece(self, fairy_piece, desired_pos):
        """
        Should enter the fairy pieces in play.
        :param fairy_piece:
        :param desired_pos:
        :return: False if fairy-piece move is not allowed or enter the piece in desired position and return True
        Additional Note: Takes two parameters [1] A string that represent the type of the piece (white falcon 'F',
        white hunter 'H', black falcon 'f', black hunter 'h') and [2] The square it will enter on its first play.
        If the fairy piece is not allowed to enter this position at this turn for any reason, it should just return
        False. Otherwise, it should enter the board at that position, update whose
        turn it is, and return True.
        """
        if self._game_state != 'UNFINISHED':
            return False

        current_turn = self._turn

        # if it's not their
        if fairy_piece.isupper() and current_turn == 'BLACK':
            return False
        elif fairy_piece.islower() and current_turn == 'WHITE':
            return False

        # check whether the player has lost a queen, a rook, a bishop, or a knight
        if current_turn == 'WHITE':
            number_of_relevant_pieces = 0
            for row in self._board:
                for piece in row:
                    if piece == 'Q' or piece == 'R' or piece == 'B' or piece == 'N' or piece == 'H' or piece == 'F':
                        number_of_relevant_pieces += 1
        elif current_turn == 'BLACK':
            number_of_relevant_pieces = 0
            for row in self._board:
                for piece in row:
                    if piece == 'q' or piece == 'r' or piece == 'b' or piece == 'n' or piece == 'h' or piece == 'f':
                        number_of_relevant_pieces += 1

        if number_of_relevant_pieces == 7:  # they haven't lost enough relevant pieces
            return False

        # check whether the fairy piece can enter the board at that position (first row rows for the player)
        # 1. if it's the first two rows
        # 2. if it's an empty space

        desired_pos_row, desired_pos_column = self.mapping_function(desired_pos)

        if current_turn == 'WHITE':
            if desired_pos_row != 6 and desired_pos_row != 7:
                return False
        elif current_turn == 'BLACK':
            if desired_pos_row != 0 and desired_pos_row != 1:
                return False

        # enter the fairy piece
        self._board[desired_pos_row][desired_pos_column] = fairy_piece

        # update fairy piece list in class
        self._fairy_pieces.remove(fairy_piece)

        if self._turn == 'WHITE':
            self._turn = 'BLACK'
            # print("It is black's turn now")
        else:
            self._turn = 'WHITE'
            # print("It is white's turn now")

    def mapping_function(self, string_position):
        # how the board is stored inside python is different to how we conventionally name the tiles in Chess
        mapping_dictionary = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            '8': 0,
            '7': 1,
            '6': 2,
            '5': 3,
            '4': 4,
            '3': 5,
            '2': 6,
            '1': 7
        }

        column_in_board = string_position[0]  # gives us 'c', for example, from 'c2'
        row_in_board = string_position[1]  # gives us '2', for example, from 'c2'

        # passing it through our mapping dictionary, so we can access the relevant position from the board:
        column_in_board_mapped = mapping_dictionary[column_in_board]
        row_in_board_mapped = mapping_dictionary[row_in_board]

        return row_in_board_mapped, column_in_board_mapped

    def get_piece_at_position(self, row_in_board_mapped, column_in_board_mapped):
        # string_position is something like 'c2', or 'b4' (that the player will enter when making a move)
        # in this function we want to get the piece at that position
        piece = self._board[row_in_board_mapped][column_in_board_mapped]
        return piece

    # SCENARIO 6: Determining the current  of the game
    def get_game_state(self):
        black_king_captured = False
        white_king_captured = False

        # Iterate through the board to find kings
        for row in self._board:
            if 'k' in row:
                black_king_captured = True
            if 'K' in row:
                white_king_captured = True

        # Determine game status
        if not black_king_captured:
            return "WHITE_WON"
        elif not white_king_captured:
            return "BLACK_WON"
        else:
            return "UNFINISHED"

    def board_limits(self, row, col):
        """
        Checks if the given row and column position is within the bounds of the chessboard.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def check_move_validity(self, piece, prev_row, next_row, prev_column, next_column):
        """
        Checks the validity of a move in the Chess game
        """
        # check if the start and end position are the same
        # print("flag -1")
        if prev_row == next_row and prev_column == next_column:
            # print("flag 0")
            return False

        if not self.board_limits(prev_row, prev_column) or not self.board_limits(next_row, next_column):
            return False

        # PAWN MOVEMENT
        if piece.lower() == 'p':  # Pawn
            # print("flag 1")
            if prev_column == next_column:  # Forward movement
                # print("flag 2")
                if piece.isupper():  # White Pawn
                    # print("prev_row: ", prev_row)
                    # print("next_row: ", next_row)
                    # print("piece at next position: ", self._board[next_row][next_column])

                    if prev_row - next_row == 1 and self._board[next_row][next_column] == ' ':  # Moving forward once
                        return True
                #  Below, we check if pawn is in its starting position, if it's moving 2 spaces forward, and if the
                #  square it moves over is empty
                    if prev_row == 6 and prev_row - next_row == 2 and self._board[next_row + 1][next_column] == ' ':
                        return True
                else:  # Black Pawn
                    if next_row - prev_row == 1 and self._board[next_row][next_column] == ' ':  # Moving forward once
                        return True
                #  Below, we check if pawn is in its starting position, if it's moving 2 spaces forward, and if the
                #  square it moves over is empty
                    if prev_row == 1 and next_row - prev_row == 2 and self._board[next_row - 1][next_column] == ' ':
                        return True

            elif abs(prev_column - next_column) == 1:  # Checks how many columns the pawn moves horizontally, and
                # ensures it is only one space horizontally

                if piece.isupper():  # White Pawn
                    if prev_row - next_row == 1 and self._board[next_row][next_column].islower():  # Checks if White
                        # Pawn is moving upwards
                        return True
                else:  # Black Pawn
                    if next_row - prev_row == 1 and self._board[next_row][next_column].isupper():  # Checks if Black
                        # Pawn is moving downwards
                        return True
            return False

        # ROOK MOVEMENT
        elif piece.lower() == 'r':  # Rook
            # Horizontal movement
            if prev_row == next_row:
                step = 1 if prev_column < next_column else -1  # Checks the direction of movement for columns
                # (moving left or right)
                for col in range(prev_column + step, next_column, step):  # Checks if there are no pieces in the Rook's
                    # way of horizontal movement and
                    # returns false if blocked
                    if self._board[prev_row][col] != ' ':
                        return False
                return True

            elif prev_column == next_column:
                step = 1 if prev_row < next_row else -1  # Checks the direction of movement for rows (moving up or down)
                for row in range(prev_row + step, next_row, step):
                    if self._board[row][prev_column] != ' ':  # Checks if there are no pieces in the Rook's way of
                        # vertical movement and returns false if blocked
                        return False
                return True
            return False

        # KNIGHT MOVEMENT
        elif piece.lower() == 'n':  # Knight
            # Knight movement: moves in an "L" shape
            row_change = abs(prev_row - next_row)  # Calculates absolute difference in rows
            column_change = abs(prev_column - next_column)  # Calculates absolute difference in columns
            if (row_change == 2 and column_change == 1) or (
                    row_change == 1 and column_change == 2):  # Checks if the movement is the intended L shape
                return True
            return False

        # BISHOP MOVEMENT
        elif piece.lower() == 'b':  # Bishop
            if abs(prev_row - next_row) == abs(prev_column - next_column):  # Checks diagonal movement
                step_row = 1 if next_row > prev_row else -1  # Checks row movement direction (upward or downwards)
                step_col = 1 if next_column > prev_column else -1  # Checks row movement direction (left or right)
                row, col = prev_row + step_row, prev_column + step_col  # Initializes variables to check diagonally
                while row != next_row:  # Iterates through diagonal path
                    if self._board[row][col] != ' ':  # Checks if there's a piece in Bishop's way
                        return False
                    row += step_row  # Checks next square in diagonal path
                    col += step_col  # Checks next square in diagonal path
                return True
            return False

        # QUEEN MOVEMENT
        elif piece.lower() == 'q':  # Queen
            # Can move vertically, horizontally, or diagonally (any number of spaces)
            # prev_row == next_row is vertical movement, prev_column == next_column means horizontal movement, and
            # abs(prev_row - next_row) == abs(prev_column - next_column means diagonal movement
            if prev_row == next_row or prev_column == next_column or abs(prev_row - next_row) == abs(prev_column - next_column):
                # Below, we check for row direction of movement
                jump_row = 1 if next_row > prev_row else -1 if next_row < prev_row else 0
                # Below, we check for column direction movement
                jump_column = 1 if next_column > prev_column else -1 if next_column < prev_column else 0
                row, col = prev_row + jump_row, prev_column + jump_column  # Initializes adjacent to start position
                while row != next_row or col != next_column:
                    if self._board[row][col] != ' ':  # Checks if there's something in the Queen's way
                        return False
                    row += jump_row  # Check the next square in given direction (by incrementing row by one)
                    col += jump_column  # Check the next square in given direction (by incrementing column by one)
                return True
            return False

        # HUNTER MOVEMENT
        elif piece.lower() == 'h':
            # Hunter moves forward like a rook (horizontally or vertically) or backward like a bishop (diagonally)
            row_difference = abs(prev_row - next_row)
            col_difference = abs(prev_column - next_column)
            if (row_difference == 0 and col_difference > 0) or (row_difference > 0 and col_difference == 0) or (
                    row_difference == col_difference):
                return True
            return False

        elif piece.lower() == 'f':  # Falcon
            # Falcon moves forward like a bishop (diagonally) or backward like a rook (vertically)
            row_diff = abs(prev_row - next_row)
            col_diff = abs(prev_column - next_column)
            if (row_diff == col_diff) or (prev_column - next_column):
                return True
            return False

        # KING MOVEMENT
        elif piece.lower() == 'k':  # King
            row_change = abs(prev_row - next_row)
            column_change = abs(prev_column - next_column)
            return (row_change == 1 and column_change <= 1) or (column_change == 1 and row_change == 0) or (
                        row_change == 1 and column_change == 1)

        else:
            return False


"""
# Example usage
chess_game = ChessVar()
chess_game.display_board()  # Display the initial board

# To make a move, convert board positions to start and end coordinates (e.g., "e2" to "e4")
# chess_game.make_move("f1", "e4")  # Example move

chess_game.make_move("f2", "f3")
chess_game.display_board()

chess_game.make_move("d7", "d5")
chess_game.display_board()

chess_game.make_move("c2", "c3")
chess_game.display_board()

chess_game.make_move("d5", "d4")
chess_game.display_board()

chess_game.make_move("h2", "h4")
chess_game.display_board()

chess_game.make_move("d4", "c3")
chess_game.display_board()

chess_game.make_move("d1", "a4")
chess_game.display_board()

chess_game.make_move("d8", "d2")
chess_game.display_board()

chess_game.make_move("a4", "a6")
chess_game.display_board()

chess_game.make_move("b7", "a6")
chess_game.display_board()

chess_game.enter_fairy_piece("H", 'f2')
chess_game.display_board()

chess_game.make_move('g7','g6')
chess_game.display_board()

chess_game.make_move('e2','e4')
chess_game.display_board()

chess_game.make_move('e7','e5')
chess_game.display_board()

chess_game.make_move('f2','e2')
chess_game.display_board()

chess_game.make_move('f7','f5')
chess_game.display_board()

chess_game.make_move('e2','e3')
chess_game.display_board()
"""
