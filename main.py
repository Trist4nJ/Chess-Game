from board import *
from pieces import *

if __name__ == "__main__":
    board = Board()
    b = Bishop('white', 7, 2, 'B')
    p1 = Pawn('white', 6, 1, 'P')
    p2 =  Pawn('black', 1, 0, 'p')
    board.move_piece(p1, 5, 1)

    board.move_piece(b, 4, 5)

    board.print_board()

