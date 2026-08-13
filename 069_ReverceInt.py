
# Reverce Int (Medium).
# https://leetcode.com/problems/reverse-integer/

# tage an int (positiv or negativ), and return it with digit inverted (as type int), if the value is over or under range 2^31 (range int), than return 0.


import math

class Solution:
    def reverse(self, x: int) -> int:
        
        reverce_abs_x = int(str(abs(x))[::-1])
        if reverce_abs_x > 2 ** 31:
            return 0
        return reverce_abs_x * (1 if x >= 0 else -1)