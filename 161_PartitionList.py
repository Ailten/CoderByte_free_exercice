
# partition list
# https://leetcode.com/problems/partition-list/

class ListNode:
    def __init__(self, val:int=0, next:"ListNode"=None):
        self.val = val
        self.next = next

def func(h: ListNode, target: int) -> ListNode:

    def pushNode(node: ListNode|None, val: int) -> ListNode:
        if node == None:
            return ListNode(val)
        node.next = ListNode(val)
        return node.next
    
    left = None
    right = None
    e = h
    first_left = None
    first_right = None

    # loop on e.
    while e != None:

        if e.val < target:
            left = pushNode(left, e.val) # push val.
            if first_left == None:
                first_left = left

        else:
            right = pushNode(right, e.val) # push val.
            if first_right == None:
                first_right = right

        e = e.next # move to next.

    # conect both.
    left.next = first_right

    return first_left


a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(3)
a.next.next.next = ListNode(2)
a.next.next.next.next = ListNode(5)
a.next.next.next.next.next = ListNode(2)
result = func(a, 3)
vals = []
while result != None:
    vals.append(result.val)
    result = result.next
print(vals)
#             v
# from : [1,4,3,2,5,2]
# to   : [1,2,2,4,3,5]
#                 ^
