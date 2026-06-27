

# Unique Path 2.
# https://leetcode.com/problems/unique-paths-ii/

# same but this can be have obstacle on grid (making some path un-reachable).



def func(map: list[list[int]]) -> int:

    # browse paths.
    pos_reach = [(0,0,1)]  # (x, y, path_reach).

    amount_of_cel_by_path = len(map)-1 + len(map[0])-1
    for _ in range(amount_of_cel_by_path):

        # browse next celules reach.
        next_pos_reach = []
        for pos_r in pos_reach:
            next_pos = (pos_r[0]+1, pos_r[1])
            if next_pos[0] < len(map[0]) and map[next_pos[1]][next_pos[0]] == 0:
                next_pos_reach.append((next_pos[0], next_pos[1], pos_r[2]))
            next_pos = (pos_r[0], pos_r[1]+1)
            if next_pos[1] < len(map) and map[next_pos[1]][next_pos[0]] == 0:
                next_pos_reach.append((next_pos[0], next_pos[1], pos_r[2]))
        
        # merge cellules reach.
        pos_reach = []
        for npr in next_pos_reach:
            val_find = next([ (k,v) for k,v in enumerate(pos_reach) if v[0] == npr[0] and v[1] == npr[1] ].__iter__(), None)
            if val_find == None:
                pos_reach.append(npr)
                continue
            pos_reach[val_find[0]] = (npr[0], npr[1], npr[2] + val_find[1][2])

    return pos_reach[0][2]


print(func([   # 4.
    [0,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,0],
]))
print(func([   # 3.
    [0,0,0,1],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,0],
]))