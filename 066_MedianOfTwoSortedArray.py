
# Median Of Two Sorted Array (Hard).
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# get two array of int (sorted), return the median of both.



class Solution:
    def findMedianSortedArrays(self, num1: list[int], num2: list[int]) -> float:
        
        index_median = (len(num1) + len(num2)) // 2

        i = 0 if len(num1) > 0 else None
        j = 0 if len(num2) > 0 else None
        last_values = [0, 0]
        for k in range(index_median+1):
            if i == None:
                last_values[k%2] = num2[j]
                j += 1
                if j == len(num2):
                    j = None
                continue
            elif j == None:
                last_values[k%2] = num1[i]
                i += 1
                if i == len(num1):
                    i = None
                continue

            v1 = num1[i]
            v2 = num2[j]
            is_i_lower = v1 < v2
            if is_i_lower:
                last_values[k%2] = v1
                i += 1
                if i == len(num1):
                    i = None
                continue
            else:
                last_values[k%2] = v2
                j += 1
                if j == len(num2):
                    j = None
                continue

        if (len(num1) + len(num2)) %2 == 0:
            return sum(last_values) / 2
        return last_values[index_median % 2]
    


# more opti, and more simple (first idee, but suposed less opti).
class Solution:
    def findMedianSortedArrays(self, num1: list[int], num2: list[int]) -> float:
        
        l = num1 + num2
        l.sort()
        i = len(l) // 2
        if len(l) % 2 == 0:
            return (l[i-1] + l[i]) / 2
        return l[i]


