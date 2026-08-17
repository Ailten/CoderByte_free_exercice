
# validate binary search tree
# https://leetcode.com/problems/validate-binary-search-tree/description/


# ---> basic tree node example.
#from typing import Optional
#class TreeNode:
#    def __init__(self, val:int=0, left: Optional["TreeNode"]=None, right:Optional["TreeNode"]=None):
#        self.val = val
#        self.left = left
#        self.right = right


from TreeNode import TreeNode
    

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