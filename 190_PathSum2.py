
# Path Sum 2
# https://leetcode.com/problems/path-sum-ii/


from TreeNode import TreeNode


def pathSum(root: TreeNode|None, target_sum: int) -> list[list[int]]:

    # same but with a parameter to get the path browse in memory (recurs).
    def getPathSum(root: TreeNode|None, target_sum: int, val_browe: list[int]|None = None) -> list[list[int]]:

        if root == None:
            return []

        target_decreased = target_sum - root.val
        if target_decreased < 0:
            return []

        is_end_leaf = root.left == None and root.right == None
        val_browe = (val_browe or []) + [root.val]
        if (
            target_decreased == 0 and 
            is_end_leaf
        ):
            return [val_browe]  # find a path valid.

        return (
            getPathSum(root.left, target_decreased, val_browe) +
            getPathSum(root.right, target_decreased, val_browe)
        )
    
    return getPathSum(root, target_sum)


print(pathSum(TreeNode.fromList([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))  # [[5,4,11,2],[5,8,4,5]].
print(pathSum(TreeNode.fromList([1,2,3]), 5))  # [].