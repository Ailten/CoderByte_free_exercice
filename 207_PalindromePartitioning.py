
# palindrome partitioning
# https://leetcode.com/problems/palindrome-partitioning/


from HashableList import HashableList

def partition(s: str) -> list[list[str]]:

    def isPalindrome(st: str) -> bool:
        return st == st[::-1]
    
    if len(s) == 1:
        return [[s]]
    if len(s) == 2:
        out = [list(s)]
        if isPalindrome(s):
            out.append([s])
        return out
    
    out = set()
    if isPalindrome(s):
        out.add([s])

    for cut_i in range(1, len(s)):
        s_left = s[:cut_i]
        s_right = s[cut_i:]

        result_right = partition(s_right)
        result_left = partition(s_left)
        for rr in result_right:
            for rl in result_left:
                out.add(HashableList(rl + rr))

    # remove double.
    #out_set = set()
    #for o in out:
    #    out_set.add(HashableList(o))
    #out = list(out_set)

    return list(out)


print(partition('aab'))  # [["a","a","b"],["aa","b"]].
print(partition('a'))  # [["a"]].
print(partition('aabb'))  # [["a","a","b","b"],["aa","b","b"]],["a", "a","bb"],["aa", "bb"]].