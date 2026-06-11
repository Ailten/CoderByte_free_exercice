
# Longest Valid Parentheses.
#

# https://leetcode.com/problems/longest-valid-parentheses/

import re

def func(s: str) -> int:

    count = 0

    while True:

        i_open = re.search(r'\(', s)
        if i_open == None:
            break
        i_open_index = i_open.span()[0]
        s = s[:i_open_index] + s[i_open_index + 1:]

        i_close = re.search(r'\)', s)
        if i_close == None:
            break
        i_close_index = i_close.span()[0]
        s = s[:i_close_index] + s[i_close_index + 1:]

        count += 2


    return count
    


print(func("(()"))  # 2.  -> "()".
print(func(")()())"))  # 4.  -> "()()".
print(func("(("))  # 0.  -> "".
