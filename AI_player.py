from board import Board
import copy

def evaluation(board_obj):
    board = board_obj.board
    square_values = [
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.7, 0.8, 1.0, 1.2, 1.2, 1.0, 0.8, 0.7],
        [0.7, 0.9, 1.3, 1.5, 1.5, 1.3, 0.8, 0.7],
        [0.7, 0.9, 1.3, 1.5, 1.5, 1.3, 0.8, 0.7],
        [0.7, 0.8, 1.0, 1.2, 1.2, 1.0, 0.8, 0.7],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    ]

    king_position_penalty = [
        [1.0, 1.0, 0.9, 0.8, 0.8, 0.9, 1.0, 1.0],
        [1.0, 0.9, 0.8, 0.7, 0.7, 0.8, 0.9, 1.0],
        [0.9, 0.8, 0.6, 0.5, 0.5, 0.6, 0.8, 0.9],
        [0.8, 0.7, 0.5, 0.3, 0.3, 0.5, 0.7, 0.8],
        [0.8, 0.7, 0.5, 0.3, 0.3, 0.5, 0.7, 0.8],
        [0.9, 0.8, 0.6, 0.5, 0.5, 0.6, 0.8, 0.9],
        [1.0, 0.9, 0.8, 0.7, 0.7, 0.8, 0.9, 1.0],
        [1.0, 1.0, 0.9, 0.8, 0.8, 0.9, 1.0, 1.0],
    ]

    pieces_values = {
        'p': -1, 'P': 1,
        'b': -3, 'B': 3,
        'n': -3, 'N': 3,
        'r': -5, 'R': 5,
        'q': -9, 'Q': 9,
        'k': -100, 'K': 100
    }

    global_score = 0
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.':
                mobility = len(get_legal_moves(piece, board_obj))
                mobility_bonus = 0.1 * mobility

                square_bonus = square_values[i][j]
                base = pieces_values[piece.name]

                if piece.name.lower() == 'k':
                    # Pénalisation de position centrale du roi
                    square_bonus *= king_position_penalty[i][j]

                global_score += base * square_bonus + (mobility_bonus if piece.color == 'white' else -mobility_bonus)

    return round(global_score, 2)



def get_legal_moves(piece, board_obj):
    legal_moves = []
    for x in range(8):
        for y in range(8):
            if piece.is_valid_move(x, y, board_obj):
                legal_moves.append((x, y))
    return legal_moves

def get_best_move(board_obj):
    board = board_obj.board
    best_score = float('inf')
    best_move = None

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece != '.' and piece.color == "black":
                legal_moves = get_legal_moves(piece, board_obj)
                for new_x, new_y in legal_moves:
                    # On simule le mouvement
                    board_copy = copy.deepcopy(board_obj)
                    piece_copy = board_copy.board[x][y]
                    board_copy.move_piece(piece_copy, new_x, new_y)

                    score = evaluation(board_copy)

                    if score < best_score:
                        best_score = score
                        best_move = (piece, new_x, new_y)

    return best_move  # (piece, x, y)
