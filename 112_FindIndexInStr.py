
# take two string, return the index start of ocurrence of the second one in the first one. if no find return -1.


import re

def strStr(haystack: str, needle: str) -> int:

    match_find = re.search(needle, haystack)
    return -1 if match_find == None else match_find.span()[0]


print(strStr('__test__', 'test'))  # 2
print(strStr('__te_t__', 'test'))  # -1

print('___________ V2')

def strStrV2(haystack: str, needle: str) -> int:

    for i in range(0, len(haystack)-len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1


print(strStrV2('__test__', 'test'))  # 2
print(strStrV2('__te_t__', 'test'))  # -1
