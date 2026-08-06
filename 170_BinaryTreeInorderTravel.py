
# Binary Tree Inorder Traversel
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

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
    
    def toListFromLeft(self) -> list[int]:
        if self.left == None and self.right == None:
            return [self.val]
        list_left = [] if self.left == None else self.left.toListFromLeft()
        list_right = [] if self.right == None else self.right.toListFromLeft()
        return list_left + [self.val] + list_right
    
    # for debuging.
    def toStr(self) -> str:
        if self.left == None and self.right == None:
            return str(self.val)
        s: list[str] = [str(self.val)]
        root: list[TreeNode|None] = [self]
        while True:
            new_root: list[TreeNode|None] = []
            for r in root:
                if r == None:
                    new_root.append(None)
                    new_root.append(None)
                    continue
                new_root.append(r.left)
                new_root.append(r.right)
            new_s: list[str] = []
            for nr in new_root:
                new_s.append('_' if nr == None else str(nr.val))
            if len([ e for e in new_s if e != '_']) == 0:
                break
            s.append(' '.join(new_s))
            root = new_root

        return '\n'.join(s)
        
        

def inorderTraversal(root: TreeNode|None) -> list[int]:

    if root == None:
        return []
    
    return root.toListFromLeft()
    


# ---> test for debug generate TreeNode.
#vv = TreeNode(1)
#vv.right = TreeNode(2)
#vv.right.left = TreeNode(3)
#print(vv.toStr())
#print(TreeNode.fromList([1,None,2,3]).toStr())

print(inorderTraversal(TreeNode.fromList([1,None,2,3])))  # [1,3,2].
#      1
#    /   \
#   _      2
#         / \
#        3   _
#
# 1 . _ 2 . 3 _  # from array (stage by stage).
#   _  1 3 2 _  # from left to right.

print(inorderTraversal(TreeNode.fromList([1,2,3,4,5,None,8,None,None,6,7,9])))  # [4,2,6,5,7,1,3,9,8].
#               1
#            /     \
#        2              3
#      /   \          /   \
#    4       5      _       8
#   / \     / \            / \
#  _   _   6   7          9   _
#
# 1 . 2 3 . 4 5 _ 8 . _ _ 6 7 9 _  # from array (stage by stage).
#  _ 4 _ 2 6 5 7 1 ___  3 9 8 _  # from left to right.