
# distinct subsequences
# https://leetcode.com/problems/distinct-subsequences/


import re

from HashableList import HashableList

def numDistinct(s: str, t: str) -> int:

    match_browse: set[HashableList[int]] = set()
    for t_i in range(len(t)):
        letter_t = t[t_i]

        # find the first match letter t.
        if t_i == 0:
            for match_first_letter in re.finditer(letter_t, s):
                index_match = match_first_letter.span()[0]
                match_browse.add(HashableList([index_match]))
            continue

        # skip if nothing matche.
        elif len(match_browse) == 0:
            break

        # extend previous path match.
        new_match_browse: set[HashableList[int]] = set()
        for mb in match_browse:
            last_mb_index = mb[len(mb)-1]
            
            for match_letter in re.finditer(letter_t, s[last_mb_index+1:]):
                index_next_letter = match_letter.span()[0] + last_mb_index+1
                new_match_browse.add(HashableList(mb.copy() + [index_next_letter]))

        match_browse = new_match_browse

    # debug.
    #print('--- debug ---')
    #for mb in match_browse:
    #    mb_str = ''
    #    for i in range(len(s)):
    #        mb_str += s[i] if i in mb else '_'
    #    print(mb_str)

    return len(match_browse)


print(numDistinct(s = "rabbbit", t = "rabbit"))  # 3.
# rabb_it
# rab_bit
# ra_bbit
print(numDistinct(s = "babgbag", t = "bag"))  # 5.
# ba_g___
# ba____g
# b____ag
# __b__ag
# ____bag