from pieces import Pawn, King, Queen, Knight, Bishop, Rook, Piece
from typing import List, Union

class Board:
    def __init__(self):
        self.board = []
        self.init_board()

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
        self.board[new_x][new_y] = piece
        self.board[piece.x][piece.y] = '.'
        piece.x = new_x
        piece.y = new_y

        if isinstance(piece, Pawn):
            piece.first_move = False

            # Promotion automatique en dame
            if (piece.color == 'white' and new_x == 0) or (piece.color == 'black' and new_x == 7):
                self.board[new_x][new_y] = Queen(piece.color, new_x, new_y, 'Q' if piece.color == 'white' else 'q')
                print(f"{piece.color.capitalize()} pawn promoted to Queen!")

    def is_square_attacked(self, x, y, color):
        for row in self.board:
            for piece in row:
                if piece != '.' and piece.color != color:
                    if piece.is_valid_move(x, y, self.board):
                        return True
        return False
