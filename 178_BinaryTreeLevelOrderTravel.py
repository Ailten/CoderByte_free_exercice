
# Binary Tree Level Order Travel
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from TreeNode import TreeNode

def levelOrder(root: TreeNode) -> list[list[int]]:

    output: list[list[int]] = []

    roots: list[TreeNode|None] = [root]
    while len(roots) > 0:

        new_roots: list[TreeNode|None] = []
        new_stage_val = []
        for r in roots:
            new_stage_val.append(r.val)

            if r.left != None:
                new_roots.append(r.left)
            if r.right != None:
                new_roots.append(r.right)

        output.append(new_stage_val)

        roots = new_roots

    return output


print(levelOrder(TreeNode.fromList([3,9,20,None,None,15,7])))  # [[3],[9,20],[15,7]].