
# Zig Zag Convertion (Medium).
# https://leetcode.com/problems/zigzag-conversion/

# take a string, and a length (value int), and return the string as doing a zig zag on the length Y send.



# PAYPALISHIRING
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# PAHNAPLSIIGYIR




class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        l = [ (s[i], self.evalI(i, numRows)) for i in range(len(s)) ]
        l.sort(key=lambda e: e[1])
        return ''.join([ e[0] for e in l ])

    def evalI(self, i: int, numRows: int) -> int:
        mod = numRows + numRows - 2
        mod_i = i % mod
        mod_half = mod // 2
        if mod_i <= mod_half:
            return mod_i
        return mod_half - (mod_i - mod_half)