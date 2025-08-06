import copy

pieces_values = {
    'p': -100, 'P': 100,
    'b': -340, 'B': 340,
    'n': -320, 'N': 320,
    'r': -500, 'R': 500,
    'q': -900, 'Q': 900,
    'k': -10000, 'K': 10000
}

def evaluation(board_obj):

    board = board_obj.board

    pawn_values = [
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.7, -50, -50, -50, -50, -50, -50, 0.7],
        [0.7, 1.0, -50, -60, -60, -50, 1.0, 0.7],
        [0.7, 1.0, -50, -60, -60, -50, 1.0, 0.7],
        [0.7, -75, -75, -75, -75, -75, -75, 0.7],
        [-99, -99, -99, -99, -99, -99, -99, -99],
        [-99, -99, -99, -99, -99, -99, -99, -99]
    ]

    knight_values = [
        [100, 100, 100, 100, 100, 100, 100, 100],
        [100, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 100],
        [100, -20, 1.0, 1.2, 1.2, 1.0, -20, 100],
        [100, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 100],
        [100, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 100],
        [100, -20, 1.0, 1.2, 1.2, 1.0, -20, 100],
        [100, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 100],
        [100, 100, 100, 100, 100, 100, 100, 100]
    ]

    bishop_values = [
        [1.5, 1.0, 0.5, 0.5, 0.5, 0.5, 1.0, 0.5],
        [0.6, -20, 0.8, 0.9, 0.9, 0.8, -20, 0.6],
        [0.7, 1.5, 1.0, 1.2, 1.2, 1.0, 1.5, 0.7],
        [0.7, 1.0, 1.2, 1.0, 1.0, 1.2, 1.0, 0.7],
        [0.7, 1.0, 1.2, 1.0, 1.0, 1.2, 1.0, 0.7],
        [0.7, 1.0, 1.0, 1.2, 1.2, 1.0, 1.0, 0.7],
        [0.6, -20, 0.8, 0.9, 0.9, 0.8, -20, 0.6],
        [0.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 1.5]
    ]

    rook_values = [
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.7, 1.5, 1.0, 1.2, 1.2, 1.0, 1.5, 0.7],
        [0.7, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 0.7],
        [0.7, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 0.7],
        [0.7, 1.0, 1.0, 1.2, 1.2, 1.0, 1.0, 0.7],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    ]

    queen_values = [
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.7, 1.5, 1.0, 1.2, 1.2, 1.0, 1.5, 0.7],
        [0.7, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 0.7],
        [0.7, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 0.7],
        [0.7, 1.0, 1.0, 1.2, 1.2, 1.0, 1.0, 0.7],
        [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    ]

    king_values = [
        [-600, -600, -500, 0.0, 0.0, 0, -600, -600],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ]

    if get_number_pieces(board_obj) <= 6:
        king_values = [
            [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
            [0.7, 1.5, 1.0, 1.2, 1.2, 1.0, 1.5, 0.7],
            [0.7, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 0.7],
            [0.7, 1.0, 1.2, 1.5, 1.5, 1.2, 1.0, 0.7],
            [0.7, 1.0, 1.0, 1.2, 1.2, 1.0, 1.0, 0.7],
            [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.6],
            [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        ] # vérifier le nombre de pièces pour déterminer si c'est en finale et donc mettre en jeu le roi

    """king_position_penalty = [
        [-1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, -1.0],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
    ]"""

    position_bonus = {
        'P': pawn_values,
        'N': knight_values,
        'B': bishop_values,
        'R': rook_values,
        'Q': queen_values,
        'K': king_values
    }

    global_score = 0
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.':
                global_score += pieces_values[piece.name] + (position_bonus[piece.name.upper()][i][j])
                if piece.name.upper() == 'P':
                    pass
    global_score -= get_developped_black_pieces(board_obj) * 20

    get_attacked_squares(board_obj, 'black')

    return round(global_score, 2)

#######################################
def get_legal_moves(piece, board_obj):
    legal_moves = []
    for x in range(8):
        for y in range(8):
            if piece.is_valid_move(x, y, board_obj):
                legal_moves.append((x, y))
    return legal_moves

def get_developped_black_pieces(board_obj):
    board = board_obj.board
    developped_pieces = 0
    for x in range(8):
        if board[0][x] == '.':
            developped_pieces += 1
    return developped_pieces

def get_number_pieces(board_obj):
    board = board_obj.board
    nb_pieces = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != '.' and board[i][j].name.upper() != 'P':
                nb_pieces += 1
    return nb_pieces

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

def get_attacked_squares(board_obj, color):
    attacked = {}  # (x, y): [valeur_piece_qui_attaque]
    board = board_obj.board
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.' and piece.color != color:
                for (x, y) in get_legal_moves(piece, board_obj):
                    if (x, y) not in attacked:
                        attacked[(x, y)] = []
                    attacked[(x, y)].append(pieces_values[piece.name])
    return attacked

# si une piece avec une valeur inférieure à celle de board[i][j] menace d'aller sur cette case, il faut :
# soit manger la pièce menaçante avec une piece d'une valeur inférieure ou égale
# soit bouger la pièce sur board[i][j] vers une case non attaquée par une pièce de valeur inférieure
