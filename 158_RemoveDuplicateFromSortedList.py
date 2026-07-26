
# remove duplicates from sorted list.
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, val:int=0, next:"ListNode"=None):
        self.val = val
        self.next = next

def func(head: ListNode) -> ListNode:

    current_node = head
    while current_node != None:
        next_node = current_node.next
        next_val = None if next_node == None else next_node.val

        if current_node.val == next_val:
            current_node.next = next_node.next
            continue

        current_node = current_node.next
    return head



# ---> example 1.
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)
result = func(a)
vals = []
while result != None:
    vals.append(result.val)
    result = result.next
print(vals)  # [1,2]

# ---> example 2.
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(3)
result = func(a)
vals = []
while result != None:
    vals.append(result.val)
    result = result.next
print(vals)  # [1,2,3]