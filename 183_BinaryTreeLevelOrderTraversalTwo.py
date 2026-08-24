

# skip 106

# binary tree level order traversal 2
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


from TreeNode import TreeNode

def levelOrderBottom(root: TreeNode) -> list[list[int]]:

    return root.toListByStage(is_remove_empty=True)[::-1]


print(levelOrderBottom(TreeNode.fromList([3,9,20,None,None,15,7])))