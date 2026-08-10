
# validate binary search tree
# https://leetcode.com/problems/validate-binary-search-tree/description/

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
    
    def __iter__(self):
        yield self.left
        yield self.right
    

def isValidBST(root: TreeNode) -> bool:

    if root.left != None:
        left_val = root.left.val
        if left_val >= root.val:
            return False
        if not isValidBST(root.left):
            return False

    if root.right != None:
        right_val = root.right.val
        if right_val <= root.val:
            return False
        if not isValidBST(root.right):
            return False

    return True



print(isValidBST(TreeNode.fromList([5,1,4,None,None,3,6])))  # False.
#    5
#   / \
#  1   4
#     / \
#    3   6
# 
# False, 4 is less than 5, but at the right root.
print(isValidBST(TreeNode.fromList([2,1,4,None,None,3,6])))  # True.


# ---> v2


# not big improve, but use __iter__ override.
def isValidBST_v2(root: TreeNode) -> bool:

    for k,r in enumerate(root):  # iter on both root (left and rigth).
        is_left = k == 0
        if r != None:
            if is_left and r.val >= root.val:
                return False
            if not is_left and r.val <= root.val:
                return False
            if not isValidBST(r):
                return False

    return True

print(' --- v2 --- ')
print(isValidBST_v2(TreeNode.fromList([5,1,4,None,None,3,6])))  # False.
print(isValidBST_v2(TreeNode.fromList([2,1,4,None,None,3,6])))  # True.