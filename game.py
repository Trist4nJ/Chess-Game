from board import *
from pieces import *
from AI_player import *

class Game:
    def __init__(self):
        self.turn = 'white'
        self.en_passant_target = None  # tuple ou None
        self.white_king_moved = False
        self.black_king_moved = False
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

    def algebraic_to_matrix(self, square: str):
        col = ord(square[0].lower()) - ord('a')  # a → 0, b → 1
        row = 8 - int(square[1])  # 8 → 0, 1 → 7
        return row, col

    def matrix_to_algebraic(self, row: int, col: int):
        letter = chr(col + ord('a'))  # 0 → a, 1 → b
        number = str(8 - row)  # 0 → 8, 7 → 1
        return letter + number

    def is_king_side_castling_possible(self, board_obj, color):
        board = board_obj.board
        if color == 'white':
            if not self.white_king_moved:
                if board[7][5] != '.' and board[7][6] != '.':
                    return False
                if board[7][7] == '.' or board[7][4] == '.':
                    return False
                if self.is_check(color):
                    return False
                if board_obj.is_square_attacked(7, 5, color) or board_obj.is_square_attacked(7, 6, color):
                    return False
        else:
            if not self.black_king_moved:
                if board[0][5] != '.' and board[0][6] != '.':
                    return False
                if board[0][4] == '.' or board[0][7] == '.':
                    return False
                if self.is_check(color):
                    return False
                if board_obj.is_square_attacked(0, 5, color) or board_obj.is_square_attacked(0, 6, color):
                    return False
        return True

    def king_side_castling(self, board_obj, color):
        board = board_obj.board

        if color == 'white':
            king = board[7][4]
            rook = board[7][7]

            king.x = 7
            king.y = 6
            rook.x = 7
            rook.y = 5

            board[7][4] = '.'
            board[7][5] = rook
            board[7][6] = king
            board[7][7] = '.'
            self.white_king_moved = True

        else:
            king = board[0][4]
            rook = board[0][7]

            king.x = 0
            king.y = 6
            rook.x = 0
            rook.y = 5

            board[0][4] = '.'
            board[0][5] = rook
            board[0][6] = king
            board[0][7] = '.'
            self.black_king_moved = True

    def is_queen_side_castling_possible(self, board_obj, color):
        board = board_obj.board
        if color == 'white':
            if not self.white_king_moved:
                if board[7][1] != '.' and board[7][2] != '.' and board[7][3] != '.':
                    return False
                if board[7][0] == '.' or board[7][4] == '.':
                    return False
                if self.is_check(color):
                    return False
                if board_obj.is_square_attacked(7, 1, color) or board_obj.is_square_attacked(7, 2,color) or board_obj.is_square_attacked(7, 3, color):
                    return False
        else:
            if not self.black_king_moved:
                if board[0][1] != '.' and board[0][2] != '.' and board[0][3] != '.':
                    return False
                if board[0][0] == '.' or board[0][4] == '.':
                    return False
                if self.is_check(color):
                    return False
                if board_obj.is_square_attacked(0, 1, color) or board_obj.is_square_attacked(0, 2,color) or board_obj.is_square_attacked(0, 3, color):
                    return False
        return True

    def queen_side_castling(self, board_obj, color):
        board = board_obj.board

        if color == 'white':
            king = board[7][4]
            rook = board[7][0]

            king.x = 7
            king.y = 2
            rook.x = 7
            rook.y = 3

            board[7][0] = '.'
            board[7][1] = '.'
            board[7][2] = king
            board[7][3] = rook
            board[7][4] = '.'
            self.white_king_moved = True
        else:
            king = board[0][4]
            rook = board[0][0]

            king.x = 0
            king.y = 2
            rook.x = 0
            rook.y = 3

            board[0][0] = '.'
            board[0][1] = '.'
            board[0][2] = king
            board[0][3] = rook
            board[0][4] = '.'
            self.black_king_moved = True


    def launch_game(self):

        print("\nTo enter a move, follow this syntax:\n")
        print("'e2 e4' to move the piece in e2 to e4 or 'KC' for kingside castling)\n")
        self.board.print_board()

        while True:
            print(f"\n{self.turn.capitalize()}'s turn")

            user_input = input("Enter move: ").strip().upper()

            if user_input == "QUIT":
                break
            # King side castling command
            if user_input == 'KC' and (not self.white_king_moved if self.turn == 'white' else not self.black_king_moved):
                if self.is_king_side_castling_possible(self.board, self.turn):
                    self.king_side_castling(self.board, self.turn)
                    self.board.print_board()
                    self.switch_turn()
                else:
                    print("Kingside castling is not possible.")
                continue

            # Queen side castling command
            if user_input == 'QC':
                if self.is_queen_side_castling_possible(self.board, self.turn):
                    self.queen_side_castling(self.board, self.turn)
                    self.board.print_board()
                    self.switch_turn()
                else:
                    print("Queenside castling is not possible.")
                continue

            try:
                start_str, end_str = user_input.split()
                start_x, start_y = self.algebraic_to_matrix(start_str.lower())
                end_x, end_y = self.algebraic_to_matrix(end_str.lower())

                piece = self.board.board[start_x][start_y]

                if piece == '.':
                    print("No piece on this square.")
                    continue

                if piece.color != self.turn:
                    print("This is not your piece.")
                    continue

                if piece.is_valid_move(end_x, end_y, self.board):
                    if self.would_cause_check(piece, end_x, end_y):
                        print("Illegal move: there is a pin or the king is in check")
                        continue

                    if self.board.move_piece(piece, end_x, end_y, self):
                        if piece.name == 'K':
                            self.white_king_moved = True
                        if piece.name == 'k':
                            self.black_king_moved = True
                        self.board.print_board()
                        self.switch_turn()

                else:
                    print("Invalid move.")

            except (ValueError, IndexError):
                print("Invalid input. Please enter correct coordinates.")

            if self.is_checkmate(self.turn):
                if self.turn == "white":
                    print("Checkmate! Black wins")
                else:
                    print("Checkmate! White wins")
                break

            if self.is_stalemate(self.turn):
                print("Stalemate!")

        print("Game ended")


    def launch_game_vs_ai(self):

        print("\nTo enter a move, follow this syntax:\n")
        print("'e2 e4' to move the piece in e2 to e4 or 'KC' for kingside castling\n)")
        self.board.print_board()

        while True:
            print(f"\n{self.turn.capitalize()}'s turn")

            if self.turn == 'white':
                user_input = input("Enter move: ").strip().upper()

                if user_input == "QUIT":
                    break
                # King side castling command
                if user_input == 'KC' and (
                not self.white_king_moved if self.turn == 'white' else not self.black_king_moved):
                    if self.is_king_side_castling_possible(self.board, self.turn):
                        self.king_side_castling(self.board, self.turn)
                        self.board.print_board()
                        self.switch_turn()
                    else:
                        print("Kingside castling is not possible.")
                    continue

                # Queen side castling command
                if user_input == 'QC':
                    if self.is_queen_side_castling_possible(self.board, self.turn):
                        self.queen_side_castling(self.board, self.turn)
                        self.board.print_board()
                        self.switch_turn()
                    else:
                        print("Queenside castling is not possible.")
                    continue

                try:
                    start_str, end_str = user_input.split()
                    start_x, start_y = self.algebraic_to_matrix(start_str.lower())
                    end_x, end_y = self.algebraic_to_matrix(end_str.lower())

                    piece = self.board.board[start_x][start_y]

                    if piece == '.':
                        print("No piece on this square.")
                        continue

                    if piece.color != self.turn:
                        print("This is not your piece.")
                        continue

                    if piece.is_valid_move(end_x, end_y, self.board):
                        if self.would_cause_check(piece, end_x, end_y):
                            print("Illegal move: there is a pin or the king is in check")
                            continue

                        if self.board.move_piece(piece, end_x, end_y, self):
                            self.board.print_board()
                            self.switch_turn()
                    else:
                        print("Invalid move.")

                except (ValueError, IndexError):
                    print("Invalid input. Please enter two numbers between 0 and 7.")

            else:
                print("AI is thinking...")
                print(f"Evaluation: {evaluation(self.board)}")
                move = get_best_move(self.board)
                if move:
                    piece, x, y = move
                    self.board.move_piece(piece, x, y, self)
                    print(f"AI moved {piece.name} to {self.matrix_to_algebraic(x, y)}")
                    self.board.print_board()
                    self.switch_turn()
                else:
                    print("AI has no legal moves.")
                    break

            if self.is_checkmate(self.turn):
                print(f"Checkmate! {'White' if self.turn == 'black' else 'Black'} wins!")
                break

            if self.is_stalemate(self.turn):
                print("Stalemate!")
                break

        print("Game ended")