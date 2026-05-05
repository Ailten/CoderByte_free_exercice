
# Regular Expression Matching (Hard).
# https://leetcode.com/problems/regular-expression-matching/

# make a regex match, who can handle jocker (.) and multiple quantity of last char mentioned (*).


# 329/ 354.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # TODO: find a way to resolve these case : ".*..a*".
        # TODO: clean the function (or re-do it from zero), to be more clean.

        # function to compare two char (second is patern).
        def isMatchingSingleChar(char: str, char_p: str) -> bool:
            if char_p == '.':
                return True
            return char == char_p

        # reduce patern border if can be.
        while len(s) > 0 and len(p) > 0 and s[len(s)-1] == p[len(p)-1]:
            s = s[:-1]
            p = p[:-1]
        while len(p) > 0 and p[len(p)-1] != '*' and len(s) > 0:
            if isMatchingSingleChar(s[len(s)-1], p[len(p)-1]):
                s = s[:-1]
                p = p[:-1]
            else:
                return False
        while len(p) > 1 and p[1] != '*' and len(s) > 0:
            if isMatchingSingleChar(s[0], p[0]):
                s = s[1:]
                p = p[1:]
            else:
                return False

        # case when patern or string is empty.
        if len(p) == 0:
            if len(s) == 0:
                return True
            return False
        else:
            if len(s) == 0:

                while len(p) > 1 and p[1] == '*':
                    p = p[2:]

                return len(p) == 0

        # loop to eval patern on string.
        i_s = 0
        is_skip_next = False
        for i_p in range(len(p)):

            if is_skip_next:
                is_skip_next = False
                continue
            
            char_p = p[i_p]
            is_many_quantity = False
            if (i_p + 1) < len(p) and p[i_p + 1] == '*':
                is_many_quantity = True
                is_skip_next = True
            
            if not is_many_quantity:  # single char match.
                if i_s < len(s) and isMatchingSingleChar(s[i_s], char_p):
                    i_s += 1
                    continue
                return False
            else:  # many char can match (indicator of quantity '*' next to).
                while True:
                    if i_s == len(s):  # patern find the end of string.

                        # reducing patern if can be (without invalidate).
                        while i_p <= len(p) - 4 and p[i_p + 3] == '*':
                            p = p[:i_p+2] + p[i_p+4:]
                        while i_p < len(p) - 2 and isMatchingSingleChar(p[i_p+2], char_p):
                            p = p[:i_p+2] + p[i_p+3:]

                        return i_p == len(p) - 2
                    
                    if isMatchingSingleChar(s[i_s], char_p):  # patern continue (on various quantity).
                        i_s += 1
                        continue
                    else:  # patern multiple stop heer.
                        break


        return i_s == len(s) and i_p == len(p) - 1
            

