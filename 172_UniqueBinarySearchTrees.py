
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
print(numTrees(4))  # 30.


# ---> v2.

# without recursivity, more opti (keep last result in memory).
def numTrees_v2(n: int) -> int:

    if n <= 0:
        return 0
    if n <= 2:
        return n

    last_ans = 2
    pow_sum = 1
    for i in range(3, n+1):
        pow_sum += pow(last_ans, 2)
        last_ans = pow_sum
    return last_ans


print(' --- v2 ---')
print(numTrees_v2(3))  # 5.
print(numTrees_v2(4))  # 30.
# 15 is max integer string pyhton allow (over, need to use a dedicate library).