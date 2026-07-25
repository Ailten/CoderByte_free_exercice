
# search in rotated sorted array two.
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


def func(nums: list[int], target: int) -> bool:

    if len(nums) == 0:
        return False

    if nums[0] == target:
        return True
    elif len(nums) == 1:
        return False
    
    is_increment = nums[0] < target

    a = 0
    b = len(nums) // 2

    if is_increment and nums[b] > target:
        return func(nums[a:b], target)
    else:
        return func(nums[b:], target)


print(func([2,5,6,0,0,1,2], 0))  # True.
print(func([2,5,6,0,0,1,2], 3))  # False.

print(func([], 0))
print(func([1], 0))
print(func([1,1], 0))
print(func([1,0,1], 0))
print(func([0,1,1], 0))
print(func([1,1,0], 0))
print(func([1,0,1,1], 0))  # not working in this case, FIXME (can be fix by just find the rotate index, un-rotate it, and logN search).
print(func([0,1,1,1], 0))
print(func([1,1,0,1], 0))
print(func([1,1,1,0], 0))
