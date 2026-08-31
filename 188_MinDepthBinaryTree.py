
# min depth of binary tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/


from TreeNode import TreeNode


def minDepth(root: TreeNode|None) -> int:

    if root == None:
        return 0
    
    return max(minDepth(root.left), minDepth(root.right)) + 1


print(minDepth(TreeNode.fromList([3,9,20,None,None,15,7])))  # 3.
print(minDepth(TreeNode.fromList([2,None,3,None,4,None,5,None,6])))  # 5.