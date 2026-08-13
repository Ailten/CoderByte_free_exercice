

# Reverce Sub Str (Easy).
# (-)

# take a string 's' and a int 'k', and reverce the k'first char of all group of 2k.

# ex: s: abcdefgh, k: 2
# return : bacdfegh


import re

def reverceSubStr(s: str, k: int) -> str:

    # vertion one line regex.
    #return re.sub(r'([a-z]{1})'*k + '([a-z]{'+str(k)+'})', ''.join(['\\'+str(e) for e in range(k,0,-1)])+'\\'+str(k+1),s)


    arr_split = re.findall(r'[a-z]{1,'+str(2*k)+'}', s)
    for i in range(len(arr_split)):
        split = arr_split[i]
        if len(split) < 2*k:
            break
        arr_split[i] = split[:k][::-1] + split[-k:]

    return ''.join(arr_split)



print(reverceSubStr('abcdefgh', 2))


