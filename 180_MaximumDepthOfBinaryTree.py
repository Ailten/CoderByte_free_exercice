
# maximum depth of binary tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


from TreeNode import TreeNode

def maxDepth(root: TreeNode) -> int:

    if root.left == None and root.right == None:
        return 1
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
    


print(maxDepth(TreeNode.fromList([3,9,20,None,None,15,7])))  # 3.