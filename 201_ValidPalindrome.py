
# valid palindrome
# https://leetcode.com/problems/valid-palindrome/


import re

def isPalindrom(s: str) -> bool:

    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    return s == s[::-1]


print(isPalindrom('A man, a plan, a canal: Panama'))  # True.
print(isPalindrom('race a car'))  # False.
print(isPalindrom(' '))  # True.