

# Binary Tree Post Order Traversal.
# https://leetcode.com/problems/binary-tree-postorder-traversal/

from TreeNode import TreeNode

def postorderTraversal(root: TreeNode | None) -> list[int]:
    
    def postorder(r: TreeNode | None, ref_list: list[int]):

        if r == None:
            return

        if not r.isLastLeaf():
            for b in r:
                postorder(b, ref_list)
        
        ref_list.append(r.val)

    output_val = []
    postorder(root, output_val)
    return output_val

        


print(postorderTraversal(TreeNode.fromList([1,None,2,3])))  # [3,2,1].
print(postorderTraversal(TreeNode.fromList([1,2,3,4,5,None,8,None,None,6,7,9])))  # [4,6,7,5,2,9,8,3,1].
print(postorderTraversal(TreeNode.fromList([])))  # [].
print(postorderTraversal(TreeNode.fromList([1])))  # [1].
