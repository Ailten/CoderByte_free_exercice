import re

# Check A-B (Easy).
# (?)

# take a string, return true if all couple of a and b char in string is spacing by 3 char exactly.


def checkAB(line):
    length_space = 3

    arr_errors = { e for e in re.findall('[a].{0,}?[b]', line) if len(e) != length_space + 2 }
    return len(arr_errors) == 0




print(checkAB('a...b'))
print(checkAB('a..b'))
print(checkAB('a....b'))
print(checkAB('c.a...b'))
print(checkAB('a...b.c'))
print(checkAB('a...b.a...b'))
print(checkAB('a...b.a..b'))
print(checkAB('a...b.a....b'))