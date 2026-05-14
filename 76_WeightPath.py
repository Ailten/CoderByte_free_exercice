
# Weight Path (Hard).
# (None)

# take a 2D list, fill of random int, return the shortest path (making the minimum sum of cellule walk), from bottom left, to top right cellule.


class PathWeight:
    path: list[tuple]
    weight: int

    def __init__(self, path: list[tuple], weight: int):
        self.path = path
        self.weight = weight

    def extendPath(self, new_pos: tuple, new_weight: int) -> 'PathWeight':
        return PathWeight(
            self.path + [new_pos],
            self.weight + new_weight
        )
    
    @property
    def last_pos(self) -> tuple:
        return self.path[len(self.path) - 1]
    
    def __str__(self) -> str:
        return (
            f'weight: {self.weight} '+
            f'path: {self.path}'
        )



def weightPath(map: list[list[int]], pos_start: tuple|None=None, pos_end: tuple|None=None) -> list[PathWeight]:

    # set default pos start and end.
    if pos_start == None:
        pos_start = (0, len(map)-1)
    if pos_end == None:
        pos_end = (len(map[0])-1, 0)

    # directions to spread paths.
    directions = [(0,-1),(1,0),(0,1),(-1,0)]

    # brows paths.
    paths = [PathWeight([pos_start], map[pos_start[1]][pos_start[0]])]
    while True:
        
        new_paths = []
        for path in paths:
            for d in directions:
                new_pos = (
                    path.last_pos[0] + d[0],
                    path.last_pos[1] + d[1]
                )

                if (  # out of range.
                    new_pos[0] < 0 or 
                    new_pos[0] > len(map[0]) - 1 or
                    new_pos[1] < 0 or 
                    new_pos[1] > len(map) - 1
                ):
                    continue
                if new_pos in path.path:  # skip back path.
                    continue

                new_path = path.extendPath(  # make new path extended.
                    new_pos,
                    map[new_pos[1]][new_pos[0]]
                )

                same_path = next([ e for e in new_paths if (
                    e.last_pos == new_pos
                ) ].__iter__(), None)
                if same_path != None:
                    if same_path.weight > new_path.weight:  # replace.
                        new_paths.remove(same_path)
                        new_paths.append(new_path)
                    else:  # alread shortest path.
                        continue
                else:  # no same path found.
                    new_paths.append(new_path)  # add as path valid.

        # replace paths by path extended.
        paths = new_paths

        # logs.
        #print(' --- extend path --- ')
        #print('\n'.join([ str(e) for e in paths ]))

        # check if reach the end.
        path_to_end = next([ e for e in paths if e.last_pos == pos_end ].__iter__(), None)
        if path_to_end != None:
            return path_to_end

map = [
    [1,5,3,4],  #[.,.,.,o],
    [1,2,4,2],  #[o,o,o,o],
    [1,3,1,4],  #[o,.,.,.],
    [3,4,3,1]   #[o,.,.,.],
]
result = weightPath(map)
print('--- result ---')
print(result)

