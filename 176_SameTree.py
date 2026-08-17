
# same tree
# https://leetcode.com/problems/same-tree/description/

# 100.


from TreeNode import TreeNode


def isSameTree(p: TreeNode, q: TreeNode) -> bool:

    return p.isEq(q)


print(isSameTree(TreeNode.fromList([1,2,3]), TreeNode.fromList([1,2,3])))  # True.
print(isSameTree(TreeNode.fromList([1,2,3]), TreeNode.fromList([1,2,9])))  # False.