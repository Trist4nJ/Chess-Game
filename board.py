from pieces import Pawn, King, Queen, Knight, Bishop, Rook, Piece
from typing import List, Union

class Board:
    def __init__(self):
        self.board = []
        self.init_board()
        self.print_board()

    def init_board(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        self.board[0][0] = Rook('black', 0,0, 'r')
        self.board[0][1] = Knight('black', 0,1, 'n')
        self.board[0][2] = Bishop('black', 0,2, 'b')
        self.board[0][3] = Queen('black', 0,3, 'q')
        self.board[0][4] = King('black', 0,4, 'k')
        self.board[0][5] = Bishop('black', 0,5, 'b')
        self.board[0][6] = Knight('black', 0,6, 'n')
        self.board[0][7] = Rook('black', 0,7, 'r')

        self.board[7][0] = Rook('white', 7,0, 'R')
        self.board[7][1] = Knight('white', 7,1, 'N')
        self.board[7][2] = Bishop('white', 7,2, 'B')
        self.board[7][3] = Queen('white', 7,3, 'Q')
        self.board[7][4] = King('white', 7,4, 'K')
        self.board[7][5] = Bishop('white', 7,5, 'B')
        self.board[7][6] = Knight('white', 7,6, 'N')
        self.board[7][7] = Rook('white', 7,7, 'R')

        for i in range(8):
            self.board[1][i] = Pawn('black', 1, i, 'p')
            self.board[6][i] = Pawn('white', 6, i, 'P')

    def print_board(self):
        print()
        print(end='  ')
        for x in range(8):
            print(x, end= ' ')
        print()
        for i in range(8):
            print(i, end= ' ')
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()

    def move_piece(self, piece, new_x, new_y):
        if piece.is_valid_move(new_x, new_y, self.board):
           self.board[new_x][new_y] = piece
           self.board[piece.x][piece.y] = '.'
           piece.x = new_x
           piece.y = new_y

