
# balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/


from TreeNode import TreeNode


# fixme : about more precise explication of what should be do.
def isBalanced(h: TreeNode) -> bool:

    def nodeCount(r: TreeNode|None) -> int:
        if r == None:
            return 0
        return nodeCount(r.left) + nodeCount(r.right) + 1
    
    print(nodeCount(h.left))
    print(nodeCount(h.right))
    return abs(nodeCount(h.left) - nodeCount(h.right)) <= 1


print(isBalanced(TreeNode.fromList([3,9,20,None,None,15,7])))  # True.
# 3
# 9 20
# _ _ 15 7
print(isBalanced(TreeNode.fromList([1,2,2,3,3,None,None,4,4])))  # False.
# 1
# 2 2
# 3 3 _ _
# 4 4 _ _ _ _ _ _
