
# Binary Tree Level Order Travel
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional

class TreeNode:
    def __init__(self, val:int=0, left: Optional["TreeNode"]=None, right:Optional["TreeNode"]=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def fromList(l: list[int|None]) -> Optional["TreeNode"]:
        if len(l) == 0 or l[0] == None:
            return None
        head = TreeNode(l.pop(0))

        root = [head]
        while len(l) != 0:
            size_value = len(root) * 2
            values = l[:size_value] if size_value < len(l) else l

            new_root = []
            for i in range(len(values)):
                new_v = values[i]
                if new_v == None:
                    continue

                ri = i // 2
                r = root[ri]

                new_r = TreeNode(new_v)
                new_root.append(new_r)

                is_left = i % 2 == 0
                if is_left:
                    r.left = new_r
                else:
                    r.right = new_r

            root = new_root
            
            del l[:len(values)]

        return head



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