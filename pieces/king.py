from .piece import Piece

class King(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)