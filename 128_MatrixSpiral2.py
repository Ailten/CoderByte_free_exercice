
# Spiral Matrix.
# https://leetcode.com/problems/spiral-matrix/

# take a matrix of int, return an array of the numbers browse in spiral patern. (starting from the top left).


# other vertion of 49_MatrixSpiral.
def func(m: list[list[int]]) -> list[int]:

    output = []

    i_dir = 0  # index direction (right, down, left, top).
    
    while len([ l for l in m if len(l) > 0]) > 0:

        line_take = None

        if i_dir == 0 or i_dir == 2:  # pop the first or last line (right, left).
            line_take = m.pop(0 if i_dir == 0 else -1)
        else:  # pop the first or last cel of eatch line (down, top).
            line_take = []
            for l in m:
                line_take.append(l.pop(-1 if i_dir == 1 else 0))

        if i_dir >= 2:  # invert order for left and top (there is desc index order).
            line_take = line_take[::-1]

        output += line_take  # merge with the new list.

        i_dir = (i_dir +1) %4  # move to the next direction.

    return output



print(func([    # 1,2,3,6,9,8,7,4,5.
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))
print(func([    # 1,2,3,4,5,6,7,8,9.
    [1,2,3],
    [8,9,4],
    [7,6,5]
]))
print(func([    # 1,2,3,6,5,4.
    [1,2,3],
    [4,5,6]
]))

