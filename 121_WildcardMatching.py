
# Wildcard Matching.
# https://leetcode.com/problems/wildcard-matching/

# dev a patern (regex like) for "?" and "*".
# "?" == 1 char (any type).
# "*" == 0 to N char (any type).
# a char = a char.


def func(s: str, pat: str) -> bool:

    class RangeMatch:
        pattern: str
        group: str

        def __init__(self, pattern:str, group:str):
            self.pattern = pattern
            self.group = group

    matches = []

    i_s = 0
    i_pat = 0
    is_increasing = True
    while i_pat < len(pat):  # brows on string.

        if i_pat < 0:    # no valid match.
            return False
        
        current_pat = pat[i_pat]

        if is_increasing:  # when increase matches, take greedy group.

            group_find = None
            match current_pat:
                case '?':
                    if i_s >= len(s):
                        is_increasing = False
                        i -= 1
                        continue
                    group_find = s[i_s]
                case '*':
                    if i_s >= len(s):
                        group_find = ''
                    else:
                        group_find = s[i_s:]
                case _:
                    if i_s >= len(s) or s[i_s] != current_pat:
                        is_increasing = False
                        i_pat -= 1
                        continue
                    group_find = s[i_s]

            matches.append(RangeMatch(current_pat, group_find))
            i_s += len(group_find)
            i_pat += 1

        else:  # decreasing.

            match matches[i_pat].pattern:
                case '*':
                    if len(matches[i_pat].group) >= 1:
                        matches[i_pat].group = matches[i_pat].group[:-1]
                        i_s -= 1
                        is_increasing = True
                        i_pat += 1
                        continue
                
            last_match = matches.pop()
            i_s -= len(last_match.group)
            i_pat -= 1

    if i_s < len(s):
        return False
    return True

            
print(func('aa', 'a'))  # False.
print(func('aa', '*'))  # True.
print(func('cb', '?a'))  # False. (?) debug meaning on exercice description.