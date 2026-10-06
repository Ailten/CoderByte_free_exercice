
# palindrome partitioning 2
# https://leetcode.com/problems/palindrome-partitioning-ii/


from HashableList import HashableList

def minCut(s: str) -> int:

    # function from last exercice.
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
    
    # take the min cut.
    all_cut = partition(s)
    min_cut = float('inf')
    for c in all_cut:
        if len(c) < min_cut:
            min_cut = len(c)
    return min_cut - 1


print(minCut("aab"))  # 1.
print(minCut("a"))  # 0.
print(minCut("ab"))  # 1.