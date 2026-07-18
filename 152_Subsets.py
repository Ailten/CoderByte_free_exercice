
# Subsets.
# https://leetcode.com/problems/subsets/


def func(nums: list[int]) -> list[list[int]]:

    combinations = [[]]

    # loop on eatch combinations (using binary).
    combinations_max_count = 1 << len(nums)
    for i in range(1, combinations_max_count):
        combinations.append([ v for k,v in enumerate(nums) if (
            (i >> k) & 1 == 1  # check bite.
        ) ])

    return combinations


print(func([1,2,3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]].
print(func([0]))  # [[],[0]].