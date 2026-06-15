
# Sudoku Solver.
# https://leetcode.com/problems/sudoku-solver/description/

# ---> func for make border around the sudoku.
def addBorder(sudoku_grid_int: list[list[int]]) -> str:
    return '\n'.join([ (
        (
            '┌'+('───┬'*2)+'───┐\n' if kl == 0 else
            '├'+('───┼'*2)+'───┤\n' if kl%3 == 0 else ''
        ) +
        ''.join([ (
            (   
                '│' if kc%3 == 0 else ''
            ) +
            str(c) +
            (
                '│' if kc == 8 else ''
            )
        ) for kc,c in enumerate(l) ]) +
        (
            '\n└'+('───┴'*2)+'───┘' if kl == 8 else ''
        ) 
    ) for kl,l in enumerate(sudoku_grid_int) ])
# --->

from functools import reduce
import os
import time

def solvSudoku(sudoku_grid: list[list[str]]) -> list[list[int]]:

    # structur of a cellule (for back traching).
    class SudokuCel():
        values_possible: list[int]
        value: int
        is_unchangeable: bool

        def __init__(self, is_unchangeable: bool, values_possible: list[int]|None=None, value: int=0):
            self.values_possible = values_possible or list(range(1, 10))
            self.value = value
            self.is_unchangeable = is_unchangeable

        @property
        def is_unknow(self) -> bool:
            return not self.is_know
        @property
        def is_know(self) -> bool:
            return self.value in range(1, 10)

    # cast grid (to use structure SudokuCel).
    grid = [ [ SudokuCel(
        is_unchangeable = c != '.',
        value = (0 if c == '.' else int(c))
    ) for c in l ] for l in sudoku_grid ]

    # loop on eatch cels (with index i generic, for allow backtracking in two dimention).
    i = 0
    is_backtrack = False
    while i < 81:
        y = i // 9
        x = i - y * 9

        current_cel = grid[y][x]

        if current_cel.is_unchangeable:
            i += 1 if not is_backtrack else -1
            continue
        is_backtrack = False

        same_line = grid[y]
        same_column: list[SudokuCel] = reduce(
            lambda accu, c: accu + c,
            [ [ c for kc,c in enumerate(l) if kc == x ] for l in grid ],
            []
        )
        same_chunk: list[SudokuCel] = reduce(
            lambda accu, c: accu + c,
            [ (
                [ c for kc,c in enumerate(l) if kc // 3 == x // 3]
            ) for kl,l in enumerate(grid) if kl // 3 == y // 3 ],
            []
        )

        values_allowed = set(current_cel.values_possible)
        values_allowed -= set([ c.value for c in same_line if c.is_know ])
        values_allowed -= set([ c.value for c in same_column if c.is_know ])
        values_allowed -= set([ c.value for c in same_chunk if c.is_know ])
        values_allowed = list(values_allowed)
        values_allowed.sort()

        # to print in realtime the result.
        #os.system('cls' if os.name == 'nt' else 'clear')
        #print(addBorder([
        #    [ c.value for c in l]
        #for l in grid ]))
        #time.sleep(0.01)

        if len(values_allowed) == 0:
            if i == 0:
                #return [
                #    [ c.value for c in l]
                #for l in grid ]
                raise Exception('no solution possible !')
            current_cel.value = 0
            current_cel.values_possible = list(range(1, 10))
            i -= 1
            is_backtrack = True
            continue
        
        value_choose = values_allowed[0]
        current_cel.value = value_choose
        current_cel.values_possible.remove(value_choose)

        i += 1
    
    # cast grid as int values.
    grid_int = [
        [ c.value for c in l]
    for l in grid ]

    return grid_int


result = solvSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])

result_expected = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

result_bordered = addBorder(result).split('\n')
result_exp_bordered = addBorder(result_expected).split('\n')
is_success = result_bordered == result_exp_bordered

os.system('cls' if os.name == 'nt' else 'clear')

space_between_grid = 2
print('result'.ljust(13+space_between_grid, ' ') + 'expected')
for i in range(13):
    print(result_bordered[i] + (' '*space_between_grid) + result_exp_bordered[i])
print('SUCCESS' if is_success else 'ERROR')
