
# Jump Knight (Medium).
# (?)

# return all position a knight (in chest), can move.

def jumpKnight(matrix: list[list[str]], pos_knight: tuple[int, int]) -> set[tuple[int, int]]:
    
    moves = [
        (2,1), (2,-1),
        (-2,1), (-2,-1),
        (1,2), (-1,2),
        (1,-2), (-1,-2)
    ]

    is_knight_white = matrix[pos_knight[1]][pos_knight[0]] == '♞'

    pos_out = set()
    for m in moves:
        pos_destination = (
            pos_knight[0] + m[0],
            pos_knight[1] + m[1]
        )

        if(  # out of range.
            (pos_destination[0] < 0) or
            (pos_destination[0] > len(matrix[0])) or
            (pos_destination[1] < 0) or
            (pos_destination[1] > len(matrix))
        ):
            continue

        piece_dest = matrix[pos_destination[1]][pos_destination[0]]

        if piece_dest != ' ':  # pos dest is busy by a piece allie.
            if (
                (piece_dest in '♟♜♝♞♛♚' and is_knight_white) or
                (piece_dest in '♙♖♗♘♕♔' and not is_knight_white)
            ):
                continue

        pos_out |= {pos_destination}
    return pos_out
        

# ♟♜♝♞♛♚
# ♙♖♗♘♕♔
print(jumpKnight([
    '♜ ♞♛ ♜♚ ',
    '♟♟   ♟♝♟',
    '  ♟ ♟♞♟ ',  # <-- knight.
    '   ♟    ',
    '  ♗♙♙   ',
    '  ♘  ♘  ',
    '♙♙♙  ♙♙♙',
    '♖  ♕ ♖♔ '
], (5, 2)))