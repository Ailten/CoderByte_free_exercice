
# Patern Matcher (Hard).
# (/)

# take a string, return the substring longest who containe alwaise the same character.


import re

def paternMatcher(s: str) -> str:

    matches = re.findall(r'((.)\2{0,})', s)
    matches = [ m[0] for m in matches ]
    matches.sort(key=lambda e: len(e), reverse=True)
    return matches[0]


print(paternMatcher('aabbbcdd'))