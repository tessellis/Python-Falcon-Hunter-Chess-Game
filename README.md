# Python-Falcon-Hunter-Chess-Game

**Author: Tess Ellis**
**GitHub Username: tessellis**
**Date: 03/17/24**
**Project Course: CS162 - Introduction to Computer Science II**

A Class-Based Python Chess Game Variant (Hunter Falcon Chess)

Locations on the board will is specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8, as shown in this diagram:

Special rules for this variant of chess:

Each of the players in the reserve has one piece of the **Falcon** and the **Hunter**.

Falcon: moves forward like a bishop, and backward like a rook

Hunter: moves forward like a rook and backward like a bishop

The falcon and hunter start the game off the board and out of play (see diagram). Once a player loses their queen, a rook, a bishop, or a knight, they may, on any subsequent move, enter their falcon or hunter into play on any **empty square of their two home ranks**. Doing so constitutes a turn. The player becomes eligible to enter their remaining fairy piece (falcon or hunter) after losing a second piece (queen, rook, bishop, or knight)(could be anytime after losing the first piece, don’t need to be losing after entering the first fairy piece).

My ChessVar class includes the following:
* An **init method** that initializes all data members
* A method called **get_game_state** that just returns 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'. 
* A method called **make_move** that takes two parameters - strings that represent the square moved from and the square moved to.   If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has already been won, then it **just returns False**.  Otherwise it makes the indicated move, removes any captured piece, updates the game state if necessary, updates whose turn it is, and returns True.
* A method called **enter_fairy_piece** that takes two parameters - strings that represent the type of the piece (white falcon 'F', white hunter 'H', black falcon 'f', black hunter 'h') and the square it will enter. For example, enter_fairy_piece ('H', 'c1'). If the fairy piece is not allowed to enter this position at this turn for any reason, it **just returns False**.  Otherwise it enters the board at that position, updates whose turn it is, and returns True.

Here's a very simple example of how the class can be used:
```
game = ChessVar()
move_result = game.make_move('c2', 'c4')
game.make_move('g7', 'g5')
state = game.get_game_state()
```
