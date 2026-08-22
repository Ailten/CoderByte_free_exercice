
# construct binary tree from preorder and inorder traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from TreeNode import TreeNode


def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    # preorder use the same instance on eatch recursive call (pop reducing it), inorder is a new list re-build.

    if len(inorder) == 0:  # end recurs branch.
        return None

    first_pre = preorder.pop(0)  # take first value.
    i = inorder.index(first_pre)  # get index of same value.
    root = TreeNode(inorder[i])
    root.left = buildTree(preorder, inorder[:i])
    root.right = buildTree(preorder, inorder[i+1:])
    return root


print(buildTree([3,9,20,15,7], [9,3,15,20,7]).toStr())
# 3
# 9 20
# _ _ 15 7