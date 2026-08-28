
# construct binary tree from inorder and postorder traversal.
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# 106.


from TreeNode import TreeNode


def buildTree(inorder: list[int], postorder: list[int]) -> TreeNode|None:

    if len(inorder) == 0 or len(postorder) == 0:
        return None

    current_val = postorder.pop()
    root = TreeNode(current_val)
    inorder_index = inorder.index(current_val)

    # important to start by the right (due to order in postorder).
    root.right = buildTree(inorder[inorder_index+1:], postorder)  # recurs.
    root.left = buildTree(inorder[:inorder_index], postorder)  # recurs.

    return root


print(buildTree([9,3,15,20,7], [9,15,7,20,3]).toStr())  # 3,9,20,None,None,15,7.
# 3
# 9 20
# _ _ 15 7
