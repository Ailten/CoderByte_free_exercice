
# Boogle Solver (Medium).
# (?)

# take a matrix of char, and a string, determine if the word is present in the matrix (horizontal, vertical, diagonal, in both direction read).

def boogleSolver(matrix, word):

    len_y = len(matrix)
    len_x = len(matrix[0])

    for y in range(len_y - len(word) + 1):
        is_last_y = y == len_y - len(word)
        for x in range(len_x - len(word) + 1):
            is_last_x = x == len_x - len(word)

            str_try = ''
            for i in range(len(word)):
                str_try += matrix[y][x+i]
            if str_try == word:
                return True
            str_try = str_try[::-1]
            if str_try == word:
                return True

            str_try = ''
            for i in range(len(word)):
                str_try += matrix[y+i][x]
            if str_try == word:
                return True
            str_try = str_try[::-1]
            if str_try == word:
                return True

            str_try = ''
            for i in range(len(word)):
                str_try += matrix[y+i][x+i]
            if str_try == word:
                return True
            str_try = str_try[::-1]
            if str_try == word:
                return True

            str_try = ''
            for i in range(len(word)):
                str_try += matrix[y+i][x+(len(word) - 1 - i)]
            if str_try == word:
                return True
            str_try = str_try[::-1]
            if str_try == word:
                return True

            if is_last_y:
                for y_sup in range(1, len(word)):
                    str_try = ''
                    for i in range(0, len(word)):
                        str_try += matrix[y+y_sup][x+i]
                    if str_try == word:
                        return True
                    str_try = str_try[::-1]
                    if str_try == word:
                        return True

            if is_last_x:
                for x_sup in range(1, len(word)):
                    str_try = ''
                    for i in range(0, len(word)):
                        str_try += matrix[y+i][x+x_sup]
                    if str_try == word:
                        return True
                    str_try = str_try[::-1]
                    if str_try == word:
                        return True
                    
    return False



print(boogleSolver([  # True.
    ['a', 'b', 'c'],
    ['a', 'a', 'a'],
    ['a', 'a', 'a']
], 'abc'))
print(boogleSolver([  # True.
    ['a', 'a', 'a'],
    ['a', 'b', 'a'],
    ['a', 'a', 'c']
], 'abc'))
print(boogleSolver([  # False.
    ['a', 'a', 'a'],
    ['a', 'a', 'a'],
    ['a', 'a', 'a']
], 'abc'))
print(boogleSolver([  # True.
    ['a', 'a', 'a'],
    ['a', 'b', 'a'],
    ['c', 'a', 'a']
], 'abc'))