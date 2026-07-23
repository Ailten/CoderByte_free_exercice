
# word search.
# https://leetcode.com/problems/word-search/


def func(board: list[list[str]], word: str) -> bool:

    if len(word) == 0:
        return True
    if len([ l for l in board if len(l) > 0 ]) == 0:
        return False


    class PathWord:
        index_char_word: int
        pos_board: tuple[int, int]
        pos_walked: set[tuple[int, int]]

        def __init__(self, index_char_word: int, pos_board: tuple[int, int], pos_walked: set[tuple[int, int]]=None):
            self.index_char_word = index_char_word
            self.pos_board = pos_board
            self.pos_walked = pos_walked or set()

    direction = [(1,0), (-1,0), (0,1), (0,-1)]


    word_paths: list[PathWord] = []

    # find first char.
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == word[0]:
                word_paths.append(PathWord(0, (x, y)))

    # extend paths.
    while True:

        # end.
        if len(word_paths) == 0:
            return False
        if word_paths[0].index_char_word == len(word) -1:
            return True
        
        new_word_paths: list[PathWord] = []
        for path in word_paths:
            for dir in direction:
                new_y = path.pos_board[1] + dir[1]
                if new_y < 0 or new_y >= len(board):  # out of range Y.
                    continue
                new_x = path.pos_board[0] + dir[0]
                if new_x < 0 or new_x >= len(board[path.pos_board[1]]):  # out of range X.
                    continue
                if (new_x, new_y) in path.pos_walked:  # already walk on it.
                    continue
                if board[new_y][new_x] == word[path.index_char_word +1]:
                    new_word_paths.append(PathWord(  # extend path.
                        path.index_char_word +1, 
                        (new_x, new_y), 
                        path.pos_walked | {path.pos_board}
                    ))
        word_paths = new_word_paths



print(func([  # True.
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], "ABCCED"))
print(func([  # True.
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], "SEE"))
print(func([  # False.
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], "ADZ"))
print(func([  # False
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], "ABCB"))