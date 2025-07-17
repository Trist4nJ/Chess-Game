from board import *
from pieces import *

class Game:
    def __init__(self):
        self.turn = 'white'
        self.en_passant_target = None  # tuple ou None
        self.game_started = False
        self.board = Board()

    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

    def is_check(self, color):
        king_x = None
        king_y = None

        for x in range(8):
            for y in range(8):
                if isinstance(self.board.board[x][y], King) and self.board.board[x][y].color == color:
                    king_x = x
                    king_y = y

        return self.board.is_square_attacked(king_x, king_y, color)

    def is_checkmate(self, color):
        if not self.is_check(color):
            return False

        for i in range(8):
            for j in range(8):
                piece = self.board.board[i][j]
                if piece != '.' and piece.color == color:
                    for x in range(8):
                        for y in range(8):
                            if piece.is_valid_move(x, y, self.board):
                                if not self.simulate_move(piece, x, y):
                                    return False
        return True

    def is_stalemate(self, color):
        if self.is_check(color):
            return False

        for i in range(8):
            for j in range(8):
                piece = self.board.board[i][j]
                if piece != '.' and piece.color == color:
                    for x in range(8):
                        for y in range(8):
                            if piece.is_valid_move(x, y, self.board):
                                if not self.simulate_move(piece, x, y):
                                    return False
        return True

    def simulate_move(self, piece, new_x, new_y):
        # Sauvegarde l’état initial
        original_x, original_y = piece.x, piece.y
        captured_piece = self.board.board[new_x][new_y]

        # Simule le coup
        self.board.board[new_x][new_y] = piece
        self.board.board[original_x][original_y] = '.'
        piece.x, piece.y = new_x, new_y

        # Vérifie si le roi est toujours en échec
        in_check = self.is_check(piece.color)

        # Restaure l’état initial
        piece.x, piece.y = original_x, original_y
        self.board.board[original_x][original_y] = piece
        self.board.board[new_x][new_y] = captured_piece

        return in_check

    def would_cause_check(self, piece, new_x, new_y):
        # Sauvegarder la position actuelle
        original_x, original_y = piece.x, piece.y
        captured_piece = self.board.board[new_x][new_y]

        # Simuler le mouvement
        self.board.board[original_x][original_y] = '.'
        self.board.board[new_x][new_y] = piece
        piece.x, piece.y = new_x, new_y

        in_check = self.is_check(piece.color)

        # Annuler le mouvement
        self.board.board[original_x][original_y] = piece
        self.board.board[new_x][new_y] = captured_piece
        piece.x, piece.y = original_x, original_y

        return in_check

    def launch_game(self):
        self.game_started = True
        self.board.print_board()

        while self.game_started:
            print(f"\n{self.turn.capitalize()}'s turn")

            try:
                start = input("Enter the coordinates of the piece to move (e.g. '6 4'): ")
                end = input("Enter the destination coordinates (e.g. '4 4'): ")
                start_x, start_y = map(int, start.split())
                end_x, end_y = map(int, end.split())

                piece = self.board.board[start_x][start_y]

                if piece == '.':
                    print("No piece on this square.")
                    continue

                if piece.color != self.turn:
                    print("This is not your piece.")
                    continue

                if piece.is_valid_move(end_x, end_y, self.board):
                    if self.would_cause_check(piece, end_x, end_y):
                        print("Illegal move: there is a pin")
                        continue

                    if self.board.move_piece(piece, end_x, end_y, self):
                        self.board.print_board()
                        self.switch_turn()
                else:
                    print("Invalid move.")

            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 7.")

            if self.is_checkmate(self.turn):
                if self.turn == "white":
                    print("Checkmate! Black wins")
                else:
                    print("Checkmate! White wins")
                break
            command = input("Type 'q' to quit or press Enter to continue: ")
            if command.lower() == 'q':
                self.game_started = False
        print("Game ended")