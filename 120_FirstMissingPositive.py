
# First Missing Positive.
# https://leetcode.com/problems/first-missing-positive/description/

# return the smalest digit not present in the arr.

def func(arr: list[int]):

    i = 1
    while i in arr:
        i += 1
    return i


print(func([1,2,0]))  # 3.
print(func([3,4,-1,1]))  # 2.
print(func([7,8,9,11,12]))  # 1.
