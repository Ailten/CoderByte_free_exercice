
# unique binary search trees
# https://leetcode.com/problems/unique-binary-search-trees/description/

# same but calcul only the count.


def numTrees(n: int) -> int:

    if n <= 0:
        return 0
    if n <= 2:
        return n

    ans = 0
    for i in range(1, n+1):
        ans += pow(numTrees(i-1), 2)
    return ans


print(numTrees(1))  # 1.
print(numTrees(2))  # 2.
print(numTrees(3))  # 5.