
# rotate image.
# https://leetcode.com/problems/rotate-image/

# take an array of int, and return it rotated (90 degree), without create a second matrix.

import math

def func(m: list[list[int]]) -> list[list[int]]:

    # loop on up-left quarter.
    for y in range(len(m) // 2):
        for x in range(math.ceil(len(m[y]) / 2)):
            current_x = x
            current_y = y
            curr_val = None
            next_val = None

            # swap to next value (quarter).
            for _ in range(4):
                next_x = (len(m) -1) -current_y  # get next pos.
                next_y = current_x

                curr_val = curr_val if curr_val != None else m[current_y][current_x]  # get values (from temp, prevent swap error).
                next_val = m[next_y][next_x]

                m[next_y][next_x] = curr_val  # set val.

                curr_val = next_val  # re-assigne index avec val for next loop.
                current_x = next_x
                current_y = next_y

    return m



print('< result 1 >')
result = func([
    [1,2,3],  # 7,4,1
    [4,5,6],  # 8,5,2
    [7,8,9]   # 9,6,3
])
for r in result:
    print(''.join([ str(e) for e in r ]))

print('< result 2 >')
result = func([
    [ 5, 1, 9,11],  # 15,13, 2, 5
    [ 2, 4, 8,10],  # 14, 3, 4, 1
    [13, 3, 6, 7],  # 12, 6, 8, 9
    [15,14,12,16]   # 16, 7,10,11
])
for r in result:
    print(''.join([ str(e).rjust(2) for e in r ]))