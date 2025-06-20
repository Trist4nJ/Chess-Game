from board import *
from pieces import *

if __name__ == "__main__":
    board = Board()
    r = Rook('white', 7, 0, 'R')
    p1 = Pawn('white', 6, 0, 'P')
    p2 =  Pawn('black', 1, 0, 'p')
    board.move_piece(p1, 4, 0)

    board.print_board()
    board.move_piece(r, 5, 0)
    board.move_piece(p2, 3, 0)
    board.move_piece(r, 3, 0)
    board.move_piece(r, 5, 1)
    board.move_piece(r, 1, 1)
    board.move_piece(r, 0, 1)


    board.print_board()
