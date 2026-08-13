
# Inverting Matrice.
# /

# take a matric (or a 2D list) of int, and return the matrice inverted.


def invertingMatric(mat: list[list[int]]) -> list[list[int]]:

    return [ l[::-1] for l in mat[::-1] ]



print(invertingMatric([
    [1,2,3],  # [9,8,7]
    [4,5,6],  # [6,5,4]
    [7,8,9],  # [3,2,1]
]))