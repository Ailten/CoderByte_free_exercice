

from typing import Optional

class ListNode:

    def __init__(self, val: int=0, next: Optional["ListNode"]=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromList(l: list[int]) -> Optional["ListNode"]:
        if len(l) == 0:
            return None
        
        h = ListNode(l.pop(0))
        e = h
        for v in l:
            new_e = ListNode(v)
            e.next = new_e
            e = new_e
        
        return h
    
    def toList(self) -> list[int]:
        l = []
        h = self

        while h != None:
            l.append(h.val)
            h = h.next

        return l