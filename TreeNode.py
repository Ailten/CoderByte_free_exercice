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
    
    def toList(self) -> list[int]:
        l = [self.val]
        if self.left == None and self.right == None:
            return l
        
        next_stage = [self.left, self.right]
        while True:
            new_stage = []
            for r in next_stage:
                l.append(None if r == None else r.val)
                if r == None:
                    continue
                new_stage.append(r.left)
                new_stage.append(r.right)
            if len([ns for ns in new_stage if ns != None]) == 0:
                break
            next_stage = new_stage

        while l[-1] == None:  # clean last None.
            l.pop()

        return l
    
    def toListByStage(self, is_remove_empty: bool = False) -> list[list[int]]:
        if self.left == None and self.right == None:
            return [[self.val]]
        output: list[list[int]] = [[self.val]]
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
                if is_remove_empty and nr == None:
                    continue
                new_s.append('_' if nr == None else str(nr.val))
            if len([ e for e in new_s if e != '_']) == 0:
                break
            output.append(new_s)
            root = new_root

        return output
    
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
    
    def __iter__(self):
        yield self.left
        yield self.right

    def isEq(self, b: Optional["TreeNode"]) -> bool:  # TODO: implement override __eq__.
        if b == None:
            return False
        if self.val != b.val:
            return False
        
        is_s_left_none = self.left == None
        is_b_left_none = b.left == None
        is_s_right_none = self.right == None
        is_b_right_none = b.right == None
        
        if is_s_left_none ^ is_b_left_none:
            return False
        if is_s_right_none ^ is_b_right_none:
            return False
        
        if not is_s_left_none and not is_b_left_none and self.left != b.left:  # recurs.
            return False
        if not is_s_right_none and not is_b_right_none and self.right != b.right:  # recurs.
            return False

        return True
    
    def isLastLeaf(self) -> bool:
        return self.left == None and self.right == None