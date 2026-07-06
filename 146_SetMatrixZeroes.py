
# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/



def func(m: list[list[int]]) -> list[list[int]]:

    pos_zero_find_x = []
    pos_zero_find_y = []

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 0:
                pos_zero_find_x.append(x)
                pos_zero_find_y.append(y)

    for y in range(len(m)):
        for x in range(len(m[y])):
            if x in pos_zero_find_x or y in pos_zero_find_y:
                m[y][x] = 0

    return m



result = func([
    [1,1,1,1],   # [1,0,1,1],
    [1,0,1,1],   # [0,0,0,0],
    [1,1,1,1],   # [1,0,1,1],
    [1,1,1,1],   # [1,0,1,1],
])
print('\n'.join([ str(c) for c in result ]))