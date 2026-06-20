
# Max Subarray.
# https://leetcode.com/problems/maximum-subarray/description/

# find the sub array (in an array of int), who has the sum the bigest (and return the sum).
# (tips: you can igniore the fact to find exactly the subarray and focus on the bigest sum find).


def func(nums: list[int]) -> int:

    max_total = float('-inf')
    current_total = 0

    for n in nums:
        current_total += n

        if current_total < 0:
            current_total = 0

        if current_total > max_total:
            max_total = current_total

    return max_total



print(func([-2,1,-3,4,-1,2,1,-5,4]))  # 6.  --> [4,-1,2,1] is the sub array with the bigest sum.

