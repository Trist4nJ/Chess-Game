from board import Board

def evaluation(board):
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
                global_score += pieces_values[piece.name]
    return global_score


if __name__=="__main__":
    board = Board()
    print(evaluation(board.board))