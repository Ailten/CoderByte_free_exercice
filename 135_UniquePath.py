
# Unique Path.
# https://leetcode.com/problems/unique-paths/


import functools

@functools.cache
def func(x:int, y:int) -> int:

    if x < 1 or y < 1:
        return 0
    if x == 1 or y == 1:
        return 1
    if x == 2 or y == 2:
        return max(x, y)

    return func(x, y-1) + func(x-1, y)
    


print(func(2, 2))  # 2.
print(func(2, 3))  # 3.
print(func(3, 7))  # 28.
print(func(4, 4))  # 20.

# sum "amount of path for both cel can be-from".
#  1,  1,  1,  1,
#  1,  2,  3,  4,
#  1,  3,  6, 10,
#  1,  4, 10, 20