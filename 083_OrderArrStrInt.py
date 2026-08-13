
# Order Arr Str Int.
# (/)

# take a string (line with many words), and return the same line with word in an other order (all word has a number in it, base the order on it).

import re

def orderStrInt(line: str) -> str:

    words = line.split()
    words.sort(key=lambda w: str(re.search(r'[0-9]{1,}', w).group(0)))
    return ' '.join(words)


print(orderStrInt('tes1t te3st t2est'))
