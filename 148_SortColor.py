
# sort color.
# https://leetcode.com/problems/sort-colors/


def func(nums: list[int]) -> list[int]:

    while True:
        is_swap = False
        i = 0
        while i < len(nums) - 1:  # bubulle sort.
            if nums[i] > nums[i+1]:
                (nums[i], nums[i+1]) = (nums[i+1], nums[i])
                is_swap = True
            i += 1
        if not is_swap:
            break
    return nums


print(func([2,0,2,1,1,0]))  # [0,0,1,1,2,2].
print(func([2,0,1]))  # [0,1,2].
