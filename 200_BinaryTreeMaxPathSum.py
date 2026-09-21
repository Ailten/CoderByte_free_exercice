
# Binary tree maximum path sum.
# https://leetcode.com/problems/binary-tree-maximum-path-sum/


from TreeNode import TreeNode

def maxPathSum(root: TreeNode) -> int:

    def maxPathSumOneLine(head: TreeNode|None) -> int:
        if head == None:
            return 0
        sums = [(head, head.val)]
        while True:
            if len([s for s in sums if not s[0].isLastLeaf()]) == 0:
                sums.sort(key=lambda s: s[1], reverse=True)
                return sums[0][1]
            new_sums = []
            for s in sums:
                if s[0].isLastLeaf():
                    new_sums.append(s)
                    continue
                if s[0].left != None:
                    new_sums.append((
                        s[0].left,
                        s[1] + s[0].left.val
                    ))
                if s[0].right != None:
                    new_sums.append((
                        s[0].right,
                        s[1] + s[0].right.val
                    ))
            sums = new_sums

    def maxPathSumForHead(head: TreeNode) -> int:
        sumPath = head.val
        if head.left != None:
            sumPath += maxPathSumOneLine(head.left)
        if head.right != None:
            sumPath += maxPathSumOneLine(head.right)
        return sumPath
        
    sum_head = maxPathSumForHead(root)
    if root.left != None:
        sum_head = max(sum_head, maxPathSumForHead(root.left))
    if root.right != None:
        sum_head = max(sum_head, maxPathSumForHead(root.right))
    return sum_head


print(maxPathSum(TreeNode.fromList([1,2,3])))  # 6.
#   1        1
#  / \      + +
# 2   3    2   3  = 6.
print(maxPathSum(TreeNode.fromList([-10,9,20,None,None,15,7])))  # 42.
#   -10
#  /   \
# 9     20         20
#      /  \       +  +
#    15    7    15    7  = 42
