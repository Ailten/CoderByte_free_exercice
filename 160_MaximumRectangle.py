
# maximum rectangle.
# https://leetcode.com/problems/maximal-rectangle/


# brut force.
def findBigestEra(map: list[list[int]]) -> int:
    
    max_era = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                continue
            
            for y_side in range(1, len(map)-y):
                for x_side in range(1, len(map[y])-x):

                    is_area_valid = len(
                        [
                            l_crop for l_crop in
                            [ l[x:x+x_side-1] for l in map[y:y+y_side-1] ]
                            if 0 in l_crop
                        ]
                    ) == 0
                    if is_area_valid:
                        if y_side * x_side > max_era:
                            max_era = y_side * x_side

    return max_era



print(findBigestEra([  # 6.
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]))


# ---> v_2 recurcivity (from bigest expected).
def findBigestEra_v2(map: list[list[int]], size_searh: tuple[int, int]|None = None) -> int:

    if size_searh == None:
        size_searh = (len(map[0]), len(map))

    if size_searh == (0,0):
        return 0
    
    for y in range(len(map) - size_searh[1]):
        for x in range(len(map[0]) - size_searh[0]):

            is_area_valid = True
            for y_check in range(y, y+size_searh[1]):
                for x_check in range(x, x+size_searh[0]):
                    if map[y_check][x_check] == 0:
                        is_area_valid = False
                        break
                if not is_area_valid:
                    break

            if is_area_valid:
                return size_searh[0] * size_searh[1]
    
    return max(  # FIXME : max recursion call reach.
        findBigestEra_v2(map, (size_searh[0] -1, size_searh[1])),
        findBigestEra_v2(map, (size_searh[0], size_searh[1] -1))
    )



#print(findBigestEra_v2([  # 6.
#    [1,0,1,0,0],
#    [1,0,1,1,1],
#    [1,1,1,1,1],
#    [1,0,0,1,0]
#]))


# ---> v_3 weight cell.
def findBigestEra_v3(map: list[list[int]], size_searh: tuple[int, int]|None = None) -> int:

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                continue

            count_adj = 1
            if x+1 < len(map[y]) and map[y][x+1] != 0:
                count_adj += 1
            if y+1 < len(map) and map[y+1][x] != 0:
                count_adj += 1
            if x-1 >= 0 and map[y][x-1] != 0:
                count_adj += 1
            if y-1 >= 0 and map[y-1][x] != 0:
                count_adj += 1

            map[y][x] = count_adj

    # TODO: process by priority and spread.
    print('\n'.join(
        [ ','.join([ str(c) for c in l ]) for l in map ]
    ))

    return 0



print(findBigestEra_v3([  # 6.
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]))