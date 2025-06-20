from .piece import Piece
from .rook import Rook
from .bishop import Bishop

class Queen(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)

    def is_valid_move(self, new_x, new_y, board):
        temp_rook = Rook(self.color, self.x, self.y)
        temp_bishop = Bishop(self.color, self.x, self.y)

        return (
            temp_rook.is_valid_move(new_x, new_y, board) or
            temp_bishop.is_valid_move(new_x, new_y, board)
        )