
# Convert sorted array to binary search Tree.
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


from TreeNode import TreeNode

def sortedArrayToBST(nums: list[int]) -> TreeNode|None:

    if len(nums) == 0:
        return None

    mid_index = len(nums) // 2
    mid_val = nums[mid_index]
    root = TreeNode(mid_val)
    root.left = sortedArrayToBST(nums[:mid_index])  # recurs.
    root.right = sortedArrayToBST(nums[mid_index+1:])  # recurs.

    return root


print(sortedArrayToBST([-10,-3,0,5,9]).toStr())