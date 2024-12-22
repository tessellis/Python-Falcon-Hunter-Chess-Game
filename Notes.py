# Author: Tess Ellis
# GitHub username: tessellis

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
        self.game_state = 'UNFINISHED'  # Initialize the game state to 'UNFINISHED' when it begins
        # SCENARIO 2: Keeping track of turn order (see make_move function also)
        self.turn = 'WHITE'  # White always has the first turn
        self.fairy_pieces = ['F', 'H', 'f', 'h']  # Each player gets one falcon and one hunter piece (not in play yet)

        # SCENARIO 3: Keeping track of the current board position
        """
        Below, upper-case letters represent White's pieces, and lower-case letters represent Black's pieces. I'm
        thinking about using dictionaries (rather than lists) because it may end up being easier to "reference" or 
        find piece positions using dictionary syntax.
        """
        self.board = {
            'a1': 'R',
            'a2': 'N',
            'a3': 'B',
            'a4': 'Q',
            'a5': 'K',
            'a6': 'B',
            'a7': 'N',
            'a8': 'R',
            'b1': 'r',
            'b2': 'n',
            'b3': 'b',
            'b4': 'q',
            'b5': 'k',
            'b6': 'b',
            'b7': 'n',
            'b8': 'r',
        }

        def make_move(prev_pos, new_pos):
            # SCENARIO 4 & 5: Determining if a regular move is valid and if a fairy piece entering move is valid
            """
            Should move chess pieces on the board.
            Parameters:
            [1] A string that represent the square moved from
            [2] tA string that represent the squareA string that represent the square (example in comment below).

            Return false if:
            [a] Square being moved from does not contain a piece belonging to the player whose turn it is
            [b] The indicated move is not legal (conditions in progress)
            [c] The game has already been won

            Else (ideas):
            [1] Check if it's the players turn (by checking whether a white or black piece is being moved)
            [2] Check if that piece can actually move in that direction and for that number of spaces (have to know
            piece it is, what position it is at, and what position it is being asked to go to)
            [2] Make the indicated move
            [2] Remove any captured piece (if applicable)
            [3] Update the game state if necessary
            [4] Update whose turn it is
            [5] Return True.
            """
            # Example: prev_pos = 'c2'
            # Example: new_pos = 'c4'
            """
            Below, since we will be receiving a string with two indices, like 'c2', prev_column will represent the 
            column of a piece's previous position column (index 0 in string). Similarly, new_column will represent 
            the column of the desired new position for a piece.
            Prev_row will represent the row (number) of the previous position based on the received string (index 
            position 1 in string). New_row will represent the row of the desired new position for a piece.
            """
            prev_column = prev_pos[0]
            new_column = new_pos[0]

            prev_row = int(prev_pos[1])
            new_row = int(new_pos[1])

            """
            Below, I'm still figuring out how to deal with vertical and horizontal piece movement. I'm considering using 
            Unicode or ASCII values to access board squares (see below code draft). I'm struggling most with
            visualizing diagonal movement.
            """
            vertical_movement = ord(new_column) - ord(prev_column)
            if vertical_movement <= 2:
                # valid move
                pass

            horizontal_movement = new_row - prev_row
            if horizontal_movement == 0:
                # valid move
                pass
                """
                Below, we are covering the turn condition (if it's white's turn now, then it's black's turn next)
                """
                if self.turn == 'WHITE':
                    self.turn = 'BLACK'
                elif self.turn == 'BLACK':
                    self.turn = 'WHITE'

        def enter_fairy_piece(fairy_pieces, desired_entry_square):
            """
            Should enter the fairy pieces in play.
            :param fairy_pieces:
            :param desired_entry_square:
            :return: False if fairy-piece move is not allowed or enter the piece in desired position and return True
            Additional Note: Takes two parameters [1] A string that represent the type of the piece (white falcon 'F',
            white hunter 'H', black falcon 'f', black hunter 'h') and [2] The square it will enter on its first play.
            If the fairy piece is not allowed to enter this position at this turn for any reason, it should just return
            False. Otherwise, it should enter the board at that position, update whose
            turn it is, and return True.
            """

        # SCENARIO 6: Determining the current state of the game
        def get_game_stats(game_state):
            """
            Should return current game state.
            :return: 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'
            Additional Note: Since this program will not use check or checkmate, the state of the game simply depends on
            if a king has been captured. So, UNFINISHED = Active turns happening, WHITE_WON means white captured Black's
            king, and BLACK_WON means Black captured White's king.
            :param game_state: Current game state.
            """


"""
** MY PROGRAM NOTES BELOW **
Standard Chess Pieces:
*Pawn*
- Worth: 1 point.
- First Move: Moves one or two squares forward.
- Moves: Moves one square forward, but on its first move, it can move two squares forward. It captures diagonally one 
  square forward.
- Captures: What is lands on, diagonally, one square forward (left or right).

*Bishop (pointy hat)*
- Worth: 3 points.
- Moves: Any number of squares, diagonally (if not blocked by its own pieces, duh).
- Captures: Only what it lands on.

*Knight*
- Worth: 3 points.
- Moves: Only piece that can jump over other pieces. Moves one square left or right horizontally and then two squares 
  up or down vertically, OR it moves two squares left or right horizontally and then one square up or down vertically. 
- Captures: Only what it lands on.

*Rook* 
- Worth: 5 points.
- Moves: As many squares as it likes left or right horizontally, or as many squares as it likes up or down vertically 
  (as long as it isn't blocked by other pieces). Like a +.
- Captures: Only what it lands on.

*Queen*
- Worth: 9 points.
- Moves: As many squares as it likes left or right horizontally, or as many squares as it likes up or down vertically 
  (like a rook). The queen can also move as many squares as it likes diagonally (like a bishop). An easy way to remember 
  how a queen can move is that it moves like a rook and a bishop combined!
- Captures: Only what it lands on.

*King* 
- Worth: 9 points.
- Moves: Only moves one square in any direction.
- Captures: Only what it lands on.

                                              _________________________

Program Restrictions:
- No check or checkmate  (if King is captured, the game ends)
- No castling (moving the king two spaces to the left or right, while the rook on that side moves to the opposite 
  side of the king)
- En passant (pawn captures an opponent's pawn on the same rank and an adjacent file)
- Pawn promotion (pawn reaches the farthest rank from its original square (or the other side of the board)) and is
  replaced with a queen, a rook, a bishop, or a knight.

Falcon-Hunter Chess:
- Each of the players in the reserve has one piece of the Falcon and the Hunter (one additional piece of each)
- At the beginning of the game, these pieces are off board (initialize and keep track of them separately)
- Fairy Piece Play Conditions: Once a player loses their queen, rook, bishop, or knight a first time, they can enter 
  one of the two fairy pieces (constitutes a turn). They can enter their second fairy piece once they lose their second 
  queen, rook, bishop, or knight.

Fair Pieces:      
  *Falcon*
    - Initial Position: Any empty square of its home rank (queen, rook, bishop, or knight).
    - Moves: [1] Forward like a bishop (any number of squares, diagonally)
             [2] Backward like a rook (vertically)
    - Captures: Only what it lands on.
    
 *Hunter* 
    - Initial Position: Any empty square of its home rank (queen, rook, bishop, or knight).
    - Moves: [1] Forward like a rook (as many squares as it likes left or right horizontally, or as many squares as it 
                 likes up or down vertically )
             [2] Backward like a bishop (diagonally)
    - Captures: Only what it lands on.
"""