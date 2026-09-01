
# path sum
# https://leetcode.com/problems/path-sum/description/


from TreeNode import TreeNode

def hasPathSum(root: TreeNode|None, target_sum: int) -> bool:

    if root == None:
        return False

    target_decreased = target_sum - root.val
    if target_decreased == 0:
        return True
    
    return (
        hasPathSum(root.left, target_decreased) or
        hasPathSum(root.right, target_decreased)
    )


print(hasPathSum(TreeNode.fromList([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))  # True.
print(hasPathSum(TreeNode.fromList([1,2,3]), 5))  # False.