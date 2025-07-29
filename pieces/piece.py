class Piece:
    def __init__(self, color, x, y, name=None, skin=None):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.value = 0
        self.skin = skin

    def __str__(self):
        return f'{self.skin}'

    def is_valid_move(self, x, y, board):
        return 0 <= x < 8 and 0 <= y < 8

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y