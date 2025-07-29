from .piece import Piece

class Knight(Piece):
    def __init__(self, color, x, y, name=None, skin=None):
        super().__init__(color, x, y, name, skin)
        self.value = 3

    def is_valid_move(self, new_x, new_y, board_obj):
        board = board_obj.board
        dx = abs(self.x - new_x)
        dy = abs(self.y - new_y)

        if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
            return False

        if (dx, dy) not in [(1, 2), (2, 1)]:
            return False

        if board[new_x][new_y] != '.' and board[new_x][new_y].color == self.color:
            return False

        return True