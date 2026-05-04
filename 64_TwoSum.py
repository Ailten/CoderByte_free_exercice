
# Two Sum (Easy).
# https://leetcode.com/problems/two-sum/

# take an array of int and a target (int), return the couple of index who make the sum as the target.


# my first proposition.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums) -1):
            val = nums[i]
            dif_val = target - val
            i2 = next([ index_e for index_e, e in enumerate(nums) if index_e != i and e == dif_val ].__iter__(), None)
            if i2 != None:
                return [i, i2]
            



# solution optimal, who loop one time and stock previous value (in a dictionary), with the dif value as index (to find by the second element).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        
        return []