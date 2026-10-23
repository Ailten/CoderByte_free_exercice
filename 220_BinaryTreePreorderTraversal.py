
# Binary tree preorder traversal.
# https://leetcode.com/problems/binary-tree-preorder-traversal/


from TreeNode import TreeNode

def preorderTraversal(root: TreeNode | None) -> list[int]:

    if root == None:
        return []
    
    list_val = [root.val]

    if root.isLastLeaf():
        return list_val

    for b in root:
        list_val.extend(preorderTraversal(b))

    return list_val



print(preorderTraversal(TreeNode.fromList([1,None,2,3])))  # [1,2,3].
print(preorderTraversal(TreeNode.fromList([1,2,3,4,5,None,8,None,None,6,7,9])))  # [1,2,4,5,6,7,3,8,9].
print(preorderTraversal(TreeNode.fromList([])))  # [].
print(preorderTraversal(TreeNode.fromList([1])))  # [1].