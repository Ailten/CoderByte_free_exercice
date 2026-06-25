
# Rotate List.
# https://leetcode.com/problems/rotate-list/

# take a linked list, and "rotate" then to return their Nth rotation result.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def func(l: ListNode, k: int) -> ListNode:

    # eval length (and get last elem).
    first_elem = l
    last_elem = first_elem
    length = 1
    while last_elem.next != None:
        last_elem = last_elem.next
        length += 1

    # clamp over rang loop.
    k %= length
    if k == 0:
        return l
    length_element_end = (length -1) -(k-1)  # length of element from last to new last.

    # get first and last elem (of next linked list).
    last_elem_cut = first_elem
    first_elem_cut = None
    for _ in range(length_element_end-1):
        last_elem_cut = last_elem_cut.next
    first_elem_cut = last_elem_cut.next

    # cut and connect new list.
    last_elem.next = first_elem  # connect (make an infinit loop).
    last_elem_cut.next = None  # cut (mark end of the new list).

    return first_elem_cut



print('< example 1 >')
param = ListNode(1)
param.next = ListNode(2)
param.next.next = ListNode(3)
result = func(param, 1)  # 3, 1, 2.
line_print = ''
while True:
    if result == None:
        break
    if line_print != '':
        line_print += ', '
    line_print += str(result.val)
    result = result.next
print(line_print)
    
print('< example 2 >')
param = ListNode(1)
param.next = ListNode(2)
param.next.next = ListNode(3)
result = func(param, 3)  # 1, 2, 3.
line_print = ''
while True:
    if result == None:
        break
    if line_print != '':
        line_print += ', '
    line_print += str(result.val)
    result = result.next
print(line_print)
    
print('< example 3 >')
param = ListNode(1)
param.next = ListNode(2)
param.next.next = ListNode(3)
result = func(param, 7)  # 3, 1, 2.
line_print = ''
while True:
    if result == None:
        break
    if line_print != '':
        line_print += ', '
    line_print += str(result.val)
    result = result.next
print(line_print)
    
print('< example 4 >')
param = ListNode(1)
param.next = ListNode(2)
param.next.next = ListNode(3)
param.next.next.next = ListNode(4)
param.next.next.next.next = ListNode(5)
result = func(param, 8)  # 3, 4, 5, 1, 2.
line_print = ''
while True:
    if result == None:
        break
    if line_print != '':
        line_print += ', '
    line_print += str(result.val)
    result = result.next
print(line_print)