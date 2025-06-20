from .piece import Piece

class Bishop(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)

    def is_valid_move(self, new_x, new_y, board):
        dx = abs(self.x - new_x)
        dy = abs(self.y - new_y)

        if dx != dy:
            return False

        if board[new_x][new_y] == '.' or board[new_x][new_y].color != self.color:
            return True

        return False
