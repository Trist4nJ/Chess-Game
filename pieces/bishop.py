from .piece import Piece

class Bishop(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)

    def is_valid_move(self, new_x, new_y, board_obj):
        board = board_obj.board
        dx = new_x - self.x
        dy = new_y - self.y

        def path_clear():
            if abs(dx) != abs(dy):
                return False

            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1

            for i in range(1, abs(dx)):
                x = self.x + i * step_x
                y = self.y + i * step_y
                if board[x][y] != '.':
                    return False
            return True

        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            destination = board[new_x][new_y]
            if (destination == '.' or destination.color != self.color) and path_clear():
                return True

        return False

