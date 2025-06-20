from .piece import Piece

class Rook(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)

    def is_valid_move(self, new_x, new_y, board):
        def clear_path():
            dx = self.x - new_x
            dy = self.y - new_y

            mouvement = self.x if dy == 0 else self.y
            index = dx if dy == 0 else dy

            if mouvement == self.x: # mouvement vertical
                direction = 1 if dx > 0 else -1
                for i in range(1, abs(dx)):
                    if board[self.x - (i * direction)][new_y] != '.':
                        return False

            elif mouvement == self.y: # mouvement horizontal
                direction = 1 if dy > 0 else -1
                for i in range(1, abs(dy)):
                    if board[new_x][self.y - (i * direction)] != '.':
                        return False
            return True


        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if self.x != new_x and self.y != new_y:
                return False

            elif self.x == new_x or self.y == new_y:
                if (board[new_x][new_y] == '.' or board[new_x][new_y].color != self.color) and clear_path():
                    return True

        return False