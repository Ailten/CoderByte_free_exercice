
# Unique binary search trees 2
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

from typing import Optional

class TreeNode:
    def __init__(self, val:int=0, left: Optional["TreeNode"]=None, right:Optional["TreeNode"]=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def fromList(l: list[int|None]) -> Optional["TreeNode"]:
        if len(l) == 0 or l[0] == None:
            return None
        head = TreeNode(l.pop(0))

        root = [head]
        while len(l) != 0:
            size_value = len(root) * 2
            values = l[:size_value] if size_value < len(l) else l

            new_root = []
            for i in range(len(values)):
                new_v = values[i]
                if new_v == None:
                    continue

                ri = i // 2
                r = root[ri]

                new_r = TreeNode(new_v)
                new_root.append(new_r)

                is_left = i % 2 == 0
                if is_left:
                    r.left = new_r
                else:
                    r.right = new_r

            root = new_root
            
            del l[:len(values)]

        return head
    
    def toListFromLeft(self) -> list[int]:
        if self.left == None and self.right == None:
            return [self.val]
        list_left = [] if self.left == None else self.left.toListFromLeft()
        list_right = [] if self.right == None else self.right.toListFromLeft()
        return list_left + [self.val] + list_right
    
    # for debuging.
    def toStr(self) -> str:
        if self.left == None and self.right == None:
            return str(self.val)
        s: list[str] = [str(self.val)]
        root: list[TreeNode|None] = [self]
        while True:
            new_root: list[TreeNode|None] = []
            for r in root:
                if r == None:
                    new_root.append(None)
                    new_root.append(None)
                    continue
                new_root.append(r.left)
                new_root.append(r.right)
            new_s: list[str] = []
            for nr in new_root:
                new_s.append('_' if nr == None else str(nr.val))
            if len([ e for e in new_s if e != '_']) == 0:
                break
            s.append(' '.join(new_s))
            root = new_root

        return '\n'.join(s)


def generateTrees(n: int, num_ban: set[int]=set()) -> list[TreeNode|None]:

    results = []

    val_allow = set(range(1, n+1)) - num_ban
    for v in val_allow:
        val_rest = list(val_allow - {v})
        val_rest.sort()
        for cut in range(0, len(val_rest)+1):
            val_left = val_rest[:cut]
            val_right = val_rest[cut:]
            results_left = [None] if len(val_left) == 0 else generateTrees(n, set(range(1, n+1)) - set(val_left))
            results_right = [None] if len(val_right) == 0 else generateTrees(n, set(range(1, n+1)) - set(val_right))
            for vl in results_left:
                for vr in results_right:

                    new_result = TreeNode(v)
                    new_result.left = vl
                    new_result.right = vr

                    list_new_result = [e for e in new_result.toListFromLeft() if e != None]
                    is_ordered = True
                    last_val = -1
                    for e in list_new_result:
                        if last_val >= e:
                            is_ordered = False
                            break
                        last_val = e

                    if is_ordered:
                        results.append(new_result)

    return results

r = generateTrees(3)  # [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]].
for e in r:
    print(e.toStr())

#    1
#  _   2
# _ _ _ 3

#    1
#  _   3 
# _ _ 2 _

#    2
#  1   3

#    3
#  1   _
# _ 2 _ _

#    3
#  2   _
# 1 _ _ _