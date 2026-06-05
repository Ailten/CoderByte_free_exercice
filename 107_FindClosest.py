
# take a array 2D of int (one 1, many 2 and 0). and return the distance from the 1 to the closest 2 (att flying path).

import math

def func(arr: list[list[int]]) -> float:

    def getDist(pos_a: tuple[int, int], pos_b: tuple[int, int]) -> float:
        dif_x = (pos_a[0] - pos_b[0]) ** 2
        dif_y = (pos_a[1] - pos_b[1]) ** 2
        return math.sqrt(dif_x + dif_y)

    id_one_y = next([ k for k,v in enumerate(arr) if 1 in v ].__iter__(), None)
    if id_one_y == None:
        return None
    id_one_x = next([ k for k,v in enumerate(arr[id_one_y]) if v == 1 ].__iter__(), None)

    min_dist = float('inf')
    is_two_find = False
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] != 2:
                continue
            dist = getDist((x, y), (id_one_x, id_one_y))
            if dist < min_dist:
                is_two_find = True
                min_dist = dist
    return min_dist if is_two_find else None


print(func([    # 2.236...
    [2,0,2,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2],
    [0,0,0,0,1,0,0],
    [0,2,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]))