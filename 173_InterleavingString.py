
# interleaving string
# https://leetcode.com/problems/interleaving-string/description/


def isInterleave(s1: str, s2: str, s3: str) -> bool:

    if len(s1) + len(s2) != len(s3):
        return False

    i1 = 0
    i2 = 0
    i3 = 0
    while True:
        if i1 == len(s1):
            return s2[i2:] == s3[i3:]
        if i2 == len(s2):
            return s1[i1:] == s3[i3:]
        
        is_s1_fit = s3[i3] == s1[i1]
        is_s2_fit = s3[i3] == s2[i2]

        if is_s1_fit ^ is_s2_fit:

            if is_s1_fit:
                i1 += 1
            else:
                i2 += 1
            i3 += 1
        
        elif not is_s1_fit and not is_s2_fit:
            return False
        
        else:
            return (  # use recurcivity, when found both path can be use (maybe bether if use back-track algorythme).
                isInterleave(s1[i1+1:], s2[i2:], s3[i3+1:]) or
                isInterleave(s1[i1:], s2[i2+1:], s3[i3+1:])
            )
        

print(isInterleave("aab", "c", "aabc"))  # True.
print(isInterleave("aab", "c", "acab"))  # True.
print(isInterleave("aab", "c", "caab"))  # True.
print(isInterleave("aab", "c", "z"))  # False.
print(isInterleave("aab", "c", "bcaa"))  # False.
print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True.


# ---> v2.

# with back tracking.
def isInterleave_v2(s1: str, s2: str, s3: str) -> bool:

    if len(s1) + len(s2) != len(s3):
        return False

    i1 = 0
    i2 = 0
    i3 = 0
    is_back_track = False
    actions: list[tuple] = []
    while True:
        if i3 == 0 and is_back_track:
            return False
        if i1 == len(s1):
            if s3[i3:] == s2[i2:]:
                return True
            is_back_track = True
        if i2 == len(s2):
            if s3[i3:] == s1[i1:]:
                return True
            is_back_track = True

        if is_back_track:
            last_action = actions.pop()

            if last_action[0] == 1:
                i1 -= 1
            else:
                i2 -= 1
            
            if not last_action[1]:
                i3 -= 1
                continue

            if last_action[0] == 1:
                actions.append((2, False))
                i2 += 1
            else:
                actions.append((1, False))
                i1 += 1
            is_back_track = False
            continue


        c1 = s1[i1]
        c2 = s2[i2]
        c3 = s3[i3]
        is_s1_match = c1 == c3
        is_s2_match = c2 == c3

        if is_s1_match ^ is_s2_match:
            if is_s1_match:
                actions.append((1, False))
                i1 += 1
            else:
                actions.append((2, False))
                i2 += 1
            i3 += 1
            continue
        
        if not is_s1_match and not is_s2_match:
            is_back_track = True
            continue

        # when have both valid, thake the s1, (and not both is valid for back track.)
        actions.append((1, True, c1))
        i1 += 1
        i3 += 1


print(' --- V2 ---')
print(isInterleave_v2("aab", "c", "aabc"))  # True.
print(isInterleave_v2("aab", "c", "acab"))  # True.
print(isInterleave_v2("aab", "c", "caab"))  # True.
print(isInterleave_v2("aab", "c", "z"))  # False.
print(isInterleave_v2("aab", "c", "bcaa"))  # False.
print(isInterleave_v2("aabcc", "dbbca", "aadbbcbcac"))  # True.