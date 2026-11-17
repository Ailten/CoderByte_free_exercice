
# contains duplicate (2).
# https://leetcode.com/problems/contains-duplicate-ii/

def containsDuplicate2(nums: list[int], k: int) -> bool:
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False

print(containsDuplicate2([1,2,3,1], 3));  # True.
print(containsDuplicate2([1,0,1,1], 1));  # True.
print(containsDuplicate2([1,2,3,1,2,3], 2));  # False.




# contains duplicate (3).
# https://leetcode.com/problems/contains-duplicate-iii/

def containsDuplicate3(nums: list[int], indexDif: int, valueDif: int) -> bool:
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if (
                abs(i - j) <= indexDiff and
                abs(nums[i] - nums[j]) <= valueDiff
            ):
                return True
    return False

print(containsDuplicate3([1,2,3,1], 3, 0));  # True.
print(containsDuplicate3([1,5,9,1,5,9], 2, 3));  # False.




