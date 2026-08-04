
# reverce linked list 2.
# https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode:
    def __init__(self, val:int=0, next:"ListNode"=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromList(l:list[int]) -> "ListNode":
        if len(l) == 0:
            return None
        h = ListNode(l[0])
        e = h
        for i in range(1, len(l)):
            e.next = ListNode(l[i])
            e = e.next
        return h
    
    def toList(self) -> list[int]:
        l = []
        e = self
        while e != None:
            l.append(e.val)
            e = e.next
        return l


def reverseBetween(h: ListNode, left:int, right:int) -> ListNode:
    
    a: ListNode|None = None
    b: ListNode|None = None
    c: ListNode|None = None
    start_a: ListNode|None = None
    last_b: ListNode|None = None
    i = 1
    e = h
    while e != None:

        if i < left:
            if a == None:
                a = ListNode(e.val)
                start_a = a
            else:
                a.next = ListNode(e.val)
                a = a.next
        elif i > right:
            c = e
            break
            #if c == None:
            #    c = ListNode(e.val)
            #else:
            #    c.next = ListNode(e.val)
            #    c = c.next
        else:
            if b == None:
                b = ListNode(e.val)
                last_b = b
            else:
                b_minus = ListNode(e.val)
                b_minus.next = b
                b = b_minus

        # increment.
        e = e.next
        i += 1

    # debug part revert.
    #print('- debug -')
    #print(None if start_a == None else start_a.toList())
    #print(None if b == None else b.toList())
    #print(None if c == None else c.toList())
    #print('- ----- -')

    # conect.
    if a != None and b != None:
        a.next = b
        if last_b != None and c != None:
            last_b.next = c

    return start_a



v = ListNode.fromList([1,2,3,4,5])
r = reverseBetween(v, 2, 4)
print(r.toList())
