
# Trapping Water (Medium).
# (?)

# take an array of int strictly positiv, represent wall (to trap water between it), and return how many water can be trap on it (max).


def trappingWater(arr):

    water_fill = 0

    is_passt_a_wall = False
    count_space_for_water = 0
    for e in arr:
        if not is_passt_a_wall:
            if e == 0:
                continue
            is_passt_a_wall = True
            count_space_for_water = 0
            continue
        if is_passt_a_wall:
            if e == 0:
                count_space_for_water += 1
                continue
            water_fill += count_space_for_water
            count_space_for_water = 0
    
    # reduce all wall.
    arr = [ max(e - 1, 0) for e in arr ]
    if sum(arr) > 0:  # can be optimise to cut when has only one element upper zero.
        water_fill += trappingWater(arr)
    
    return water_fill

    
        






print(trappingWater([3,0,1,0,2,0,1]))  # 6.
print(trappingWater([3,0,1,0,2,0,0,1]))
print(trappingWater([3,0,1,0,2,0,0,3]))