
# Find index str.
# /

# take two string, find a match of the second into the first one, and return the index where it start (or -1).

import re

def findIndexStr(a: str, b: str) -> int:

    match = re.search(b, a)
    if match == None:
        return -1
    return match.span()[0]


print(findIndexStr('aabc', 'bc'))  # 2