
# calcul the destination pos, before mapping all input direction.

def func(map: str, pos_start: tuple):

    direction = {
        '^': ( 0, -1),
        '>': ( 1,  0),
        'v': ( 0,  1),
        '<': (-1,  0)
    }
    pos_dest = pos_start
    for m in map:
        pos_dest = (
            pos_dest[0] + direction[m][0],
            pos_dest[1] + direction[m][1]
        )
    return pos_dest


print(func('<vv>^>>v', (0, 0)))  # 2,2


# ----> with draw path.
# now, draw the path walked on a 2D map.


def funcV2(map: str, pos_start: tuple):

    direction = {
        '^': ( 0, -1),
        '>': ( 1,  0),
        'v': ( 0,  1),
        '<': (-1,  0)
    }
    pos_dest = pos_start
    pos_path = {pos_dest}
    for m in map:
        pos_dest = (
            pos_dest[0] + direction[m][0],
            pos_dest[1] + direction[m][1]
        )
        pos_path |= {pos_dest}

    str_path = '\n'.join([ (
        ''.join([ (
            '#' if (x, y) in pos_path else '.'
        )for x in range(-5, 6) ]) 
    ) for y in range(-5, 6) ])
    
    return str_path


print('____________ v2')
print(funcV2('<vv>^>>v', (0, 0)))
print('____________')
print(funcV2('^<^<<<v<vvv>v>>v>>v^>>^>>^>^^^<^<<<v', (0, -1)))  # heart.