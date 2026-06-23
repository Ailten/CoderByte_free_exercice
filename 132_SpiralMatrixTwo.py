
# Spirtal Matrix 2
# https://leetcode.com/problems/spiral-matrix-ii/

# take an int N, and generate a matrix NxN fill with number from 1 to M, place in spiral patern.


def func(n: int) -> list[list[int]]:

    if n == 0:
        return []
    if n == 1:
        return [[1]]

    m = []

    m.append(list(range(1, n+1)))
    for y in range(1, n-1):
        m.append([(n-1)-y+(n*3-2)] + [None]*(n-2) + [y+n])
    m.append(list(range(n*3 -2, n*2 -2, -1)))

    if n == 2:
        return m
    
    # --> fill by browsing it circulary.
    #x = 0
    #y = 1
    #current_val = m[y][x]
    #direction_index = 0
    #directions = [(1,0),(0,1),(-1,0),(0,-1)]
    #is_last_rotate = False
    #while True:
    #
    #    current_dirtection = directions[direction_index]
    #    next_x, next_y = (x+current_dirtection[0], y+current_dirtection[1])
    #    if m[next_y][next_x] != None:  # need rotate direction.
    #        if is_last_rotate:  # 2 rotate sucessively.
    #            break  # end loop.
    #        direction_index = (direction_index + 1) % 4
    #        is_last_rotate = True
    #        continue
    #    is_last_rotate = False
    #    
    #    current_val += 1
    #    x, y = (next_x, next_y)
    #    m[y][x] = current_val
    #
    #return m

    # fill it recurcively.
    val_to_add = n*4 - 4
    center_m = func(n-2)
    for y in range(len(center_m)):
        for x in range(len(center_m[y])):
            m[y+1][x+1] = center_m[y][x] + val_to_add
    
    return m
    


print('< -- result 1 -- >')
param_n = 3
result = func(param_n)
for y in range(param_n):
    print(','.join([ str(e) for e in result[y] ]))

print('< -- result 2 -- >')
param_n = 4
result = func(param_n)
for y in range(param_n):
    print(','.join([ str(e).rjust(2,' ') for e in result[y] ]))

print('< -- result 3 -- >')
param_n = 1
result = func(param_n)
for y in range(param_n):
    print(','.join([ str(e) for e in result[y] ]))

print('< -- result 4 -- >')
param_n = 0
result = func(param_n)
for y in range(param_n):
    print(','.join([ str(e) for e in result[y] ]))

print('< -- result 5 -- >')
param_n = 5
result = func(param_n)
for y in range(param_n):
    print(','.join([ str(e).rjust(2,' ') for e in result[y] ]))

print('< -- result 6 -- >')
param_n = 2
result = func(param_n)
for y in range(param_n):
    print(','.join([ str(e) for e in result[y] ]))