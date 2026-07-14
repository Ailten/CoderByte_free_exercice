
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


# ------> V2.


def func_v2(nums: list[int]) -> list[int]:

    i_min = 0
    i_max = len(nums)
    i_mid = i_max // 2

    range_a = nums[i_min:i_mid]
    range_b = nums[i_mid:i_max]

    if len(range_a) > 1:
        range_a = func_v2(range_a)
    if len(range_b) > 1:
        range_b = func_v2(range_b)

    merged_range = []  # merge sort.

    i_a = 0;
    i_b = 0;
    while True:
        if i_a == len(range_a):
            merged_range += range_b[i_b:]
            break;
        if i_b == len(range_b):
            merged_range += range_a[i_a:]
            break;

        if range_a[i_a] < range_b[i_b]:
            merged_range.append(range_a[i_a])
            i_a += 1
        else:
            merged_range.append(range_b[i_b])
            i_b += 1

    return merged_range



print(func_v2([2,0,2,1,1,0]))  # [0,0,1,1,2,2].
print(func_v2([2,0,1]))  # [0,1,2].


# ------> V3.


def func_v3(nums: list[int]) -> list[int]:

    sorted_list = []
    
    for n in nums:
        i = 0
        while i < len(sorted_list):  # can be improve by searching by subdividing 2 instead of increment.
            if sorted_list[i] > n:
                break;
            i += 1
        sorted_list.insert(i, n)
    
    return sorted_list
        


print(func_v3([2,0,2,1,1,0]))  # [0,0,1,1,2,2].
print(func_v3([2,0,1]))  # [0,1,2].


# ------> V4.


def func_v4(nums: list[int]) -> list[int]:

    return (  # work only becose are only 3 values.
        [n for n in nums if n == 0] +
        [n for n in nums if n == 1] +
        [n for n in nums if n == 2]
    )
        


print(func_v4([2,0,2,1,1,0]))  # [0,0,1,1,2,2].
print(func_v4([2,0,1]))  # [0,1,2].

