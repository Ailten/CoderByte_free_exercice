
# Surrounded regions
# https://leetcode.com/problems/surrounded-regions/


# FIXME: need to debug.
def solve(board: list[list[str]]) -> None:

    def apply(y: int, x: int, b: list[list], nb: list[list]):
        if (
            y < 0 or y >= len(b) or
            x < 0 or x >= len(b[0]) or
            b[y][x] == 'X' or
            nb[y][x]
        ):
            return
        
        nb[y][x] = True
        
        # recurs.
        adj_pos = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for adj in adj_pos:
            apply(x+adj[0], y+adj[1], b, nb)

    board_l = len(board)
    board_w = len(board[0])

    new_board = [[False] * board_w for _ in range(board_l)]

    for y in range(board_l):
        for x in range(board_w):
            if (
                (y == 0 or y == board_l -1 or x == 0 or x == board_w -1) and
                board[y][x] == 'O' and
                new_board[y][x] == False
            ):
                apply(y, x, board, new_board)

    # apply the new board.
    for y in range(board_l):
        for x in range(board_w):
            if new_board[y][x] == False:
                board[y][x] = 'X'


b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(b)
for l in b:
    print(l)