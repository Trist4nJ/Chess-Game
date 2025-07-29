from .piece import Piece

class King(Piece):
    def __init__(self, color, x, y, name=None, skin=None):
        super().__init__(color, x, y, name, skin)
        self.value = 100
        self.never_moved = True


    def is_valid_move(self, new_x, new_y, board_obj):
        board = board_obj.board
        moves = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # on saute le déplacement nul
                moves.append((dx, dy))

        destination = board[new_x][new_y]
        dx = new_x - self.x
        dy = new_y - self.y

        if (dx, dy) in moves and (destination == '.' or destination.color != self.color):
            if not board_obj.is_square_attacked(new_x, new_y, self.color):
                return True

        return False


    def queen_side_castling(self, board_obj, color):
        pass
