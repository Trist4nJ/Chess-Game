from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, x, y, name=None):
        super().__init__(color, x, y, name)
        self.first_move = True

    def is_valid_move(self, new_x, new_y, board):
        # Il reste la prise en passant à implémenter

        dx = new_x - self.x
        dy = new_y - self.y

        direction = 1 if self.color == 'white' else -1
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            # Avancer le pion de 1
            if dx == 1 * direction and new_y == self.y and board[new_x][new_y] == '.':
                return True

            # Avancer le pion de 2 si c'est le premier coup et qu'il n'y a pas de pièce sur la case intermédiaire
            elif dx == 2 * direction and new_y == self.y and board[new_x][new_y] == '.' and self.first_move and board[new_x + direction][new_y] == '.':
                self.first_move = False
                return True

            # Manger en diagonale si la nouvelle case n'est pas vide PUIS vérifier que la pièce est de couleur différente sinon erreur
            elif dx == 1 * direction and (abs(dy) == 1) and board[new_x][new_y] != '.' and self.color != board[new_x][new_y].color:
                return True

        return False


