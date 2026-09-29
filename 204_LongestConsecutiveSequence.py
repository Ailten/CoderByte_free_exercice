
# Longest consecutive sequence
# https://leetcode.com/problems/longest-consecutive-sequence/


def longestConsecutive(nums: list[int]) -> int:

    if len(nums) <= 1:
        return len(nums)

    # sanitise and order.
    nums = list(set(nums))
    nums.sort()

    last_num = nums.pop(0)
    length_following = 1
    bigest_legth = 1

    for n in nums:
        is_following = last_num + 1 == n
        if is_following:  # increaste length.
            length_following += 1
            if length_following > bigest_legth:
                bigest_legth = length_following
        else:  # reset length count.
            length_following = 1


        # end loop.
        last_num = n

    return bigest_legth


print(longestConsecutive([100,4,200,1,3,2]))  # 4.
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # 9.
print(longestConsecutive([1,0,1,2]))  # 3.