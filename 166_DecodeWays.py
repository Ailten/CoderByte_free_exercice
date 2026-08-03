
# decode ways.
# https://leetcode.com/problems/decode-ways/


import re

def numDecodings(s: str) -> int:

    # only numbers.
    if re.match('^[0-9]+$', s) == None:
        return 0
    
    def isAValidCharCode(char1: str, char2: str|None=None) -> bool:
        if char2 == None or char2 == '0':  # 1-9 -> v.  0 -> x.
            return char1 != '0'
        if char1 == '0':  # 01 -> x.
            return False
        if char1 == '1':  # 10-19 -> v.
            return True
        if char1 == '2':  # 20-26 -> v.  27-29 -> x.
            return int(char2) <= 6
        return False  # 30-90 -> x.
    
    def decode(char: str) -> str:  # 1 -> A
        return chr(int(char) + 64)
    def encode(char: str) -> str:  # A -> 1
        return str(ord(char) - 64)
    
    # fist char.
    if not isAValidCharCode(s[0]):
        return 0
    paths = [decode(s[0])]

    for i in range(1, len(s)):
        char = s[i]

        new_paths = []

        for p in paths:
            last_p_decode = encode(p[-1])

            is_can_merge = isAValidCharCode(last_p_decode, char)
            if is_can_merge:
                merged = decode(last_p_decode + char)
                new_paths.append(p[:len(p)-1] + merged)

            elif not isAValidCharCode(last_p_decode):  # ignore p if last_p is unvalid AND merged not to.
                continue
        
            new_paths.append(p + decode(char))  # can include last char not valid (for next merge).

        paths = new_paths

    # filter last char (can be not valid).
    paths = [ p for p in paths if isAValidCharCode(encode(p[-1])) ]

    # debug.
    #print(paths)

    return len(paths)



print(numDecodings('12'))   # 2. -> 1,2 / 12
print(numDecodings('226'))  # 3. -> 2,2,6 / 22,6 / 2,26
print(numDecodings('06'))   # 0. -> catch '0'
