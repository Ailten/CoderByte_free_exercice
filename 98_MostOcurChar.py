
# most ocur char.

# take a string, and return the char ocur the most time on it.

import re

def mostOcurChar(line: str) -> str:

    # without regex.
    #chars_count = dict()
    #while len(line) > 0:
    #    char = line[0]
    #    line = line[1:]
    #    chars_count[char] = chars_count.get(char, 0) + 1
    #arr_chars = [ (k, v) for k,v in chars_count.items() ]
    #arr_chars.sort(key=lambda e: e[1], reverse=True)
    #return arr_chars[0][0]

    line.sort()
    arr_chars = re.findall(r'(.)\1{0,}', line)
    arr_chars.sort(key=lambda e: len(e), reverce=True)
    return arr_chars[0][0]


print(mostOcurChar('abcdeef'))  # e
print(mostOcurChar('abbcdddeff'))  # d
print(mostOcurChar('abbfcddeff'))  # f