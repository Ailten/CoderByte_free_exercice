
# binary tree zigzag level order travel
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/



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

        if len(output) % 2 == 0:  # same as the last exercice, but reverce order of value stage when is an odd stage. 
            output.append(new_stage_val)
        else:
            output.append(new_stage_val[::-1])

        roots = new_roots

    return output


print(levelOrder(TreeNode.fromList([3,9,20,None,None,15,7])))  # [[3],[20,9],[15,7]].