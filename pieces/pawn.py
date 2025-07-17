from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)
        self.first_move = True

    def is_valid_move(self, new_x, new_y, board_obj):
        board = board_obj.board
        dx = new_x - self.x
        dy = new_y - self.y

        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1

        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            # Avance d'une case
            if dx == direction and dy == 0 and board[new_x][new_y] == '.':
                return True

            # Avance de deux cases depuis la ligne de départ
            elif dx == 2 * direction and dy == 0 and self.x == start_row:
                if board[self.x + direction][self.y] == '.' and board[new_x][new_y] == '.':
                    return True

            # Capture diagonale
            elif dx == direction and abs(dy) == 1:
                target = board[new_x][new_y]
                if target != '.' and target.color != self.color:
                    return True

        return False



