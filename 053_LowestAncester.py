
# Lowest Ancester (Medium).
# (?)

# take a binary tree, and two number, return the number of the lowest ancestor of both.

def lowestAncester(arr, to_find):
    
    left_parent = to_find[0]
    right_parent = to_find[1]

    while True:  # browse parent of left.

        while True:  # browse parent of right.

            if left_parent == right_parent:
                return right_parent

            right_parent = next([ e[1] for e in arr if e[0] == right_parent ].__iter__(), None)
            if right_parent == None:
                right_parent = to_find[1]
                break

        left_parent = next([ e[1] for e in arr if e[0] == left_parent ].__iter__(), None)
        if left_parent == None:
            left_parent = to_find[0]
            break

    return None


#       3
#     /   \
#   2       4
#  / \     / \
# 1   7   5   6
print(lowestAncester([(1,2), (2,3), (7,2), (4,3), (5,4), (6,4)], (1,7)))  # 2.
print(lowestAncester([(1,2), (2,3), (7,2), (4,3), (5,4), (6,4)], (1,5)))  # 3.
print(lowestAncester([(1,2), (2,3), (7,2), (4,3), (5,4), (6,4)], (1,4)))  # 3.
print(lowestAncester([(1,2), (2,3), (7,2), (4,3), (5,4), (6,4)], (1,9)))  # None.
