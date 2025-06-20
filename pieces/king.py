from .piece import Piece

class King(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)

    def is_valid_move(self, new_x, new_y, board):
        def is_safe():
            pass

        moves = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # on saute le déplacement nul (le roi ne reste pas sur place)
                moves.append((dx, dy))

        destination = board[new_x][new_y]
        dx = new_x - self.x
        dy = new_y - self.y

        if (dx, dy) in moves and (destination == '.' or destination.color != self.color) and is_safe():
            return True

        return False
