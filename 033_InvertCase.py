import re

# Invert Case (Easy).
# (?)

# take a string, and return it with invert eatch lower case char into upper case, and upper into lower.


def invertCase(line):

    str_out = ''
    for c in line:
        if re.search('[A-Z]', c) != None:
            str_out += c.lower()
            continue
        str_out += c.upper()

    return str_out




print(invertCase('hello word'))
print(invertCase('Hello Word'))
print(invertCase('AaA'))