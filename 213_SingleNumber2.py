
# single number 2.
# https://leetcode.com/problems/single-number-ii/


def singleNumber(nums: list[int]) -> int | None:
    
    nums.sort()  # sort to make all values match their double.

    for i in range(0, len(nums), 3):

        if i+2 >= len(nums):  # if reatch the end of list, the last "block of three" should contan the only one unique number.
            return nums[i]

        is_one_equal_two = nums[i] == nums[i+1]
        is_one_equal_three = nums[i] == nums[i+2]

        if is_one_equal_two and is_one_equal_three:  # three values are same.
            continue

        if not is_one_equal_two and not is_one_equal_three:  # one is diferent.
            return nums[i]
        if not is_one_equal_two and is_one_equal_three:  # two is diferent.
            return nums[i+1]
        return nums[i+3]  # three is diferent (last case).
    
    return None  # all values are same.


print(singleNumber([2,2,3,2]))  # 3.
print(singleNumber([0,1,0,1,0,1,99]))  # 99.