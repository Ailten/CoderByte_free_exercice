

# symmetric tree
# https://leetcode.com/problems/symmetric-tree/description/


from TreeNode import TreeNode


def isSymmetric(root: TreeNode|None) -> bool:
    
    def isBranchSymmetric(l: TreeNode|None, r: TreeNode|None) -> bool:
        if (l == None) ^ (r == None):
            return False
        if l == None and r == None:
            return True
        if l.val != r.val:
            return False
        return (
            isBranchSymmetric(l.left, r.right) and  # recurs, both, swap (for symmetric).
            isBranchSymmetric(l.right, r.left)
        )

    return isBranchSymmetric(root.left, root.right)


print(isSymmetric(TreeNode.fromList([1,2,2,3,4,4,3])))  # True.
print(isSymmetric(TreeNode.fromList([1,2,2,None,3,None,3])))  # True.