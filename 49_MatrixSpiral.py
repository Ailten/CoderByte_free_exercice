
# Matrix Spiral (Medium).
# (?)

# take a matrice, and return element in array (1D) by taking it in spiral.


def matrixSpiral(matrix):

    out = []

    pos = (0,0)
    direction = 0
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    while True:
        out.append(matrix[pos[1]][pos[0]])
        matrix[pos[1]][pos[0]] = None

        for i in range(5):
            if i == 4:
                return out
            new_pos = (
                pos[0] + directions[direction][0],
                pos[1] + directions[direction][1]
            )
            if (
                (new_pos[0] < 0 or new_pos[0] >= len(matrix)) or
                (new_pos[1] < 0 or new_pos[1] >= len(matrix)) or
                (matrix[new_pos[1]][new_pos[0]] == None)
            ):
                direction = (direction + 1) % len(directions)
                continue
            pos = new_pos
            break
        
    





print(matrixSpiral(
    [
        [1,2],
        [4,3]
    ]
))
print(matrixSpiral(
    [
        [1,2,3],
        [8,9,4],
        [7,6,5]
    ]
))