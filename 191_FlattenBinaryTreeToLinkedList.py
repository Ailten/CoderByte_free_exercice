
# Flatten Binary Tree To linked list
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from TreeNode import TreeNode

def flatten(root: TreeNode|None) -> None:

    if root == None:
        return
    
    is_has_left = root.left != None
    if is_has_left:

        # insert last left root between current node and right root.
        previous_right = root.right  # backup old right.
        root.right = root.left  # replace right by old left.
        root.left = None  # erase left.
        last_leaf_right = root.right  # get last leaf right.
        while not last_leaf_right.isLastLeaf():
            last_leaf_right = last_leaf_right.right
        last_leaf_right.right = previous_right  # re-connect old right.
    
    # recurs to the right root (include old left freshly flattened).
    flatten(root.right)


r = TreeNode.fromList([1,2,5,3,4,None,6])
print('--- tree before ---')
print(r.toStr())
# 1
# 2 5
# 3 4 _ 6
flatten(r)
print('--- tree after ---')
print(r.toStr())
# 1
# _ 2
# _ _ _ 3
# _ _ _ _ _ _ _ 4
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 5
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 6
l = []
while r != None:
    l.append(r.val)
    r = r.right
print(l)  # [1,2,3,4,5,6].