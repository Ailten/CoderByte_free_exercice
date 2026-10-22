
# Linked list cycle 2.
# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional['ListNode'] = None

def hasCycle(head: Optional[ListNode]) -> Optional[ListNode]:

    ids = []
    nodes: list[ListNode] = []
    while head != None:

        current_id = id(head)
        try:
            index_match = ids.index(current_id)
            return nodes[index_match]
        except ValueError:
            pass

        ids.append(current_id)
        nodes.append(head)

        head = head.next


    return None


print("--- test 1 ---")
node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next.next = node.next
result = hasCycle(node)
print(result if result == None else result.val)  # 2

print("--- test 2 ---")
node = ListNode(1)
node.next = ListNode(2)
node.next.next = node
result = hasCycle(node)
print(result if result == None else result.val)  # 1

print("--- test 3 ---")
node = ListNode(1)
result = hasCycle(node)
print(result if result == None else result.val)  # None

