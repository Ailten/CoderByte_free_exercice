
# Beautifull Array (?).
# (?)


# V1
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:

        arr_out = []
        i = 1
        while len(arr_out) < n:

            is_valid = True
            for a in arr_out:
                if i + a == target:
                    is_valid = False
                    break
            if is_valid:
                arr_out.append(i)

            i += 1

        return sum(arr_out)
    

s = Solution()
s.minimumPossibleSum(6, 12)
    