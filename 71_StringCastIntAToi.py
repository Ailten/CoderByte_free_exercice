
# String Cast Int AToi (Medium).
# https://leetcode.com/problems/string-to-integer-atoi/

# take a string, and cast it as int (string can contain parasit values like letters, space, + or -, and need to be clamp as int range).



import re

class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = re.sub('^[ ]{0,}', '', s, re.I)
        #s = re.sub('[+]{0,}', '', s, re.I)
        #s = re.sub('^[0]{0,}', '', s)
        s_l = re.findall('^[-+]{0,1}[0-9]{1,}', s)
        if len(s_l) == 0:
            return 0
        s = s_l[0]

        s_num = int(s)

        if s_num >= 2**31:
            s_num = 2**31 -1
        elif s_num < -2**31:
            s_num = -2**31
        return s_num