
# recover binary search tree
# https://leetcode.com/problems/recover-binary-search-tree/description/

from TreeNode import TreeNode


def recoverTree(root: TreeNode) -> TreeNode:

    package_dict: dict[str, TreeNode|None] = {
        'first': None,
        'second': None,
        'prev': None
    }

    # browse root (both side of tree, recurcively, to edit the dict param, and found 'first' and 'second' node (to swap))
    def browse(r: TreeNode|None, package: dict[TreeNode|None]):
        if r == None:
            return
        browse(r.left, package)  # recurs left.
        pr = package.get('prev')
        if pr != None and pr.val > r.val:
            package['first'] = package.get('first') or pr
            package['second'] = r
        package['prev'] = r
        browse(r.right, package)  # recurs right.

    browse(root, package_dict)  # first call.
    first = package_dict.get('first')
    second = package_dict.get('second')
    first.val, second.val = second.val, first.val  # swap.

    return root
            

print(recoverTree(TreeNode.fromList([1,3,None,None,2])).toList())  # [3,1,None,None,2].
print(recoverTree(TreeNode.fromList([3,1,4,None,None,2])).toList())  # [2,1,4,null,null,3].