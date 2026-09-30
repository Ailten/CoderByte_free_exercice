
# sum root to leaf numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/


from TreeNode import TreeNode

def sumNumbers(root: TreeNode|None) -> int:

    if root == None:
        return 0

    sum_merg = 0

    def sumPath(r: TreeNode, path: str|None=None) -> int:
        if path == None:
            path = str(r.val)

        # reach a value
        if r.isLastLeaf():
            return int(path)

        sum_merg = 0
        
        if r.left != None:
            sum_merg += sumPath(r.left, path=path+str(r.left.val))
        if r.right != None:
            sum_merg += sumPath(r.right, path=path+str(r.right.val))
        
        return sum_merg

    return sumPath(root)


print(sumNumbers(TreeNode.fromList([1,2,3])))  # 25.
print(sumNumbers(TreeNode.fromList([4,9,0,5,1])))  # 1026.