
# Charlie the Dog (Medium).
# (?)

# take a matrix of char, and find the shortest path from S (start) to E (end), can walk on char '.', can't on '#'.


def charlieTheDog(matrix: list, char_start: str='S', char_end: str='E', char_obstacle: str='#') -> list:

    pos_s = findAChar(matrix, char_start)
    
    paths = [ [ pos_s ] ]
    while True:
        new_paths = list()
        for p in paths:
            new_paths_extended = extendPathFourDirection(matrix, p, path_already_visited=paths + new_paths, cellule_to_avoid=char_obstacle)

            path_end = next([ pae for pae in new_paths_extended if matrix[pae[len(pae)-1][1]][pae[len(pae)-1][0]] == char_end ].__iter__(), None)
            if path_end != None:  # find path.
                return path_end
            
            new_paths += new_paths_extended

        if len(new_paths) == 0:  # there is no path possible.
            return None
        
        paths = new_paths





def findAChar(matrix: list, char_search: str) -> tuple:
    
    pos_find = None
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == char_search:
                pos_find = (x, y)
                break
        if pos_find != None:
            break

    return pos_find

def extendPathFourDirection(matrix: list, path: list, path_already_visited: set=set(), cellule_to_avoid: str=None) -> list:

    direction = [(0,-1), (1,0), (0,1), (-1,0)]
    path_out = list()
    for d in direction:
        last_pos = path[len(path)-1]
        new_pos = (
            last_pos[0] + d[0],
            last_pos[1] + d[1]
        )

        if (  # optimisation, by reducing path un-necessary.
            (new_pos[0] < 0) or  # out of range.
            (new_pos[0] >= len(matrix[0])) or 
            (new_pos[1] < 0) or 
            (new_pos[1] >= len(matrix)) or 
            (matrix[new_pos[1]][new_pos[0]] == cellule_to_avoid) or
            (new_pos in path) or  # avoiding making a loop walk.
            (next([ pav for pav in path_already_visited if new_pos in pav ].__iter__(), None) != None)  # avoiding duplicate path endid in the same cellule.
        ):
            continue
            
        new_path = path + [new_pos]
        path_out.append(new_path)
    return path_out




print(charlieTheDog([  # [(0,0),(1,0),(2,0),(2,1),(2,2)]
    ['S','.','.'],
    ['.','.','.'],
    ['.','.','E']
]))
print(charlieTheDog([  # [(0,0),(1,0),(2,0),(2,1),(2,2)]
    ['S','.','.'],
    ['#','#','.'],
    ['.','.','E']
]))
print(charlieTheDog([  # [(0,0),(0,1),(0,2),(1,2),(2,2)]
    ['S','#','.'],
    ['.','#','.'],
    ['.','.','E']
]))
print(charlieTheDog([  # [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2)]
    ['S','#','.','.','.'],
    ['.','#','.','#','.'],
    ['.','.','.','#','E']
]))
print(charlieTheDog([  # None
    ['S','#','.'],
    ['.','#','.'],
    ['.','#','E']
]))


