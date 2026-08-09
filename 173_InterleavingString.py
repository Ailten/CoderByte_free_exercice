
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