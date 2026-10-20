
# single number
# https://leetcode.com/problems/single-number/

# return the number who has no occure twice.


def singleNumber(nums: list[int]) -> int:

    all_values_ref = set(nums)  # get all number value (unique).
    for v in all_values_ref:  # remove one time every type of values.
        nums.remove(v)
    all_values_ref -= set(nums)  # remove from all type values the rest (every number who has doublon once).
    return next(all_values_ref.__iter__())  # get the first element (it rest only one).



print(singleNumber([2,2,1]))  # 1.
print(singleNumber([4,1,2,1,2]))  # 4.
print(singleNumber([1]))  # 1.

