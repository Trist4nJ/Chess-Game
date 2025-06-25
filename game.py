from board import *
from pieces import *

class Game:
    def __init__(self):
        self.turn = 'white'
        self.game_started = False
        self.board = Board()

    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

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

                if piece.is_valid_move(end_x, end_y, self.board.board):
                    self.board.move_piece(piece, end_x, end_y)
                    self.board.print_board()
                    self.switch_turn()
                else:
                    print("Invalid move.")

            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 7.")

            # Pour tester : sortir du jeu manuellement
            command = input("Type 'q' to quit or press Enter to continue: ")
            if command.lower() == 'q':
                self.game_started = False