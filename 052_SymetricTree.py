import math

# Symetric Tree (Medium).
# (?)

# take an array of binary info (child, parent), and determine if the tree binary is symetric or not.
# (vertion with input array of tuple, distinct values).


def symetricTree(arr) -> bool:

    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return arr[0] == arr[1]

    branch_left = arr[:len(arr) // 2]
    branch_right = arr[int(math.ceil(len(arr) / 2)):]

    pivo_left = takePivo(branch_left)
    pivo_right = takePivo(branch_right)

    if (pivo_left == None) != (pivo_right == None):
        return False
    if pivo_left != pivo_right:
        return False

    return (
        symetricTree(branch_left) and 
        symetricTree(branch_right)
    )


def takePivo(arr):
    return (arr[len(arr) // 2] if len(arr) % 2 == 1 else None)




print(symetricTree([1]))  # true.
print(symetricTree([1,1]))  # true.
print(symetricTree([1,2]))  # false.
print(symetricTree([1,2,1]))  # true.
print(symetricTree([1,2,0]))  # false.
print(symetricTree([2,5,4,2,3,5,2]))  # false.
print(symetricTree([2,5,2,1,2,5,2]))  # true.