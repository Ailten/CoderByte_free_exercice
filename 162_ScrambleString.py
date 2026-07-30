
# scramble string
# https://leetcode.com/problems/scramble-string/


def isScramble(s1: str, s2:str) -> bool:

    # check same (already right order).
    if s1 == s2:
        return True
    # check length.
    if len(s1) != len(s2):
        return False
    # check if chars is equal (erase a lot of False cases).
    s1_sort = list(s1)
    s1_sort.sort()
    s2_sort = list(s2)
    s2_sort.sort()
    if s1_sort != s2_sort:
        return False
    # check if only one char.
    if len(s1) == 1:
        return s1 == s2
    # check if only two char.
    if len(s1) == 2:
        return s1[::-1] == s2

    for i in range(1, len(s1)-1):
        s1_sub_a = s1[:i]  # cut s1.
        s1_sub_b = s1[i:]

        is_valid_without_swap = (
            isScramble(s1_sub_a, s2[:i]) and
            isScramble(s1_sub_b, s2[i:])
        )
        if is_valid_without_swap:
            return True
        
        is_valid_with_swap = (
            isScramble(s1_sub_b, s2[:len(s1_sub_b)]) and
            isScramble(s1_sub_a, s2[len(s1_sub_b):])
        )
        if is_valid_with_swap:
            return True
        
    return False


print(isScramble("great", "rgeat"))  # True.
# [gr] [eat]  # split + not swap.
# -- [[r] [g]]   # split + swap.
# -- [[e] [at]]  # split + not swap.
# ---- [[a] [t]]  # split + no swap.
# rgeat       # match.
print(isScramble("abcde", "caebd"))  # False.
print(isScramble("abcde", "bcade"))  # True.