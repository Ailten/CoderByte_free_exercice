
# Linked list cycle.
# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional['ListNode'] = None

def hasCycle(head: Optional[ListNode]) -> bool:

    ids = []
    while head != None:

        current_id = id(head)
        if current_id in ids:
            return True
        ids.append(current_id)

        head = head.next

    return False


print("--- test 1 ---")
node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next.next = node.next
print(hasCycle(node))  # True.

print("--- test 2 ---")
node = ListNode(1)
node.next = ListNode(2)
node.next.next = node
print(hasCycle(node))  # True.

print("--- test 3 ---")
node = ListNode(1)
print(hasCycle(node))  # False.

