def load_fen(fen):
    board = []
    rows = fen.split('/')
    for row in rows:
        board_row = []
        for c in row:
            if c.isdigit():
                board_row.extend(['.'] * int(c))
            else:
                board_row.append(c)
        board.append(board_row)

    for row in board:
        print(' '.join(row))  # affichage lisible

if __name__ == "__main__":
    load_fen("r1bqkb1r/1pp1pppp/p1n2n2/b7/4P3/5N2/PPPP1PPP/RNBQK2R")
