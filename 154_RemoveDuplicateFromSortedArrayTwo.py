
# remove dupliates from sorted array two.
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/



def func(nums: list[int]) -> list[int]:

    if len(nums) < 3:
        return nums

    i = 0
    val = nums[0]
    count_val = 0
    while i < len(nums):
        current_val = nums[i]

        if current_val != val:
            val = current_val
            count_val = 1
            i += 1
            continue

        count_val += 1
        if count_val >= 3:
            nums.pop(i)
            continue

        i+= 1

    return nums


print(func([1,2,3]))
print(func([1,1,2,3,3]))
print(func([1,1,1,2,3,3,3]))


# ---> v2.


# shorter and more opti.
def func_v2(nums: list[int]) -> list[int]:

    if len(nums) < 3:
        return nums

    i = 0
    while i < len(nums) - 2:
        if nums[i] == nums[i+2]:
            nums.pop(i)
            continue
        i += 1
    
    return nums


print(func_v2([1,2,3]))
print(func_v2([1,1,2,3,3]))
print(func_v2([1,1,1,2,3,3,3]))

