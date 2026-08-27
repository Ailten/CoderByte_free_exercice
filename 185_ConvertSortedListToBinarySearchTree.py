
# convert sorted list to binary search tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from TreeNode import TreeNode
from ListNode import ListNode

# from last exercice.
def sortedArrayToBST(nums: list[int]) -> TreeNode|None:

    if len(nums) == 0:
        return None

    mid_index = len(nums) // 2
    mid_val = nums[mid_index]
    root = TreeNode(mid_val)
    root.left = sortedArrayToBST(nums[:mid_index])  # recurs.
    root.right = sortedArrayToBST(nums[mid_index+1:])  # recurs.

    return root



def sortedListToBST(head: ListNode) -> TreeNode:

    l = head.toList()

    return sortedArrayToBST(l)


print(sortedListToBST(ListNode.fromList([-10,-3,0,5,9])).toStr())

