from board import *
from pieces import *

if __name__ == "__main__":
    board = Board()
    p1 = Pawn('white', 6, 1, 'P')
    p2 =  Pawn('black', 1, 0, 'p')
    k = King('white', 7, 4, 'K')
    board.move_piece(p1, 5, 1)


    board.print_board()

