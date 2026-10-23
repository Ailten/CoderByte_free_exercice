
# Reorder list.
# https://leetcode.com/problems/reorder-list/

from ListNode import ListNode

def reorderList(head: ListNode | None) -> None:

    listed: list[ListNode] = []  # to list.
    current_node = head
    while current_node != None:
        listed.append(current_node)
        current_node = current_node.next

    current_node = head
    for i in range(len(listed) // 2):

        if i != 0:  # do not take the first node (already take in head).
            current_node.next = listed[i]
            current_node = current_node.next

        reversed_i = len(listed) - 1 - i
        current_node.next = listed[reversed_i]
        current_node = current_node.next

    if len(listed) % 2 == 1:  # take the middle one, if list len is odd.
        current_node.next = listed[len(listed) // 2]
        current_node = current_node.next


    current_node.next = None  # cut the last node (prevent infinit loop).

    return head


node = ListNode.fromList([1,2,3,4,5,6,7,8])
reorderList(node)
print(node.toList())  # [1,8,2,7,3,6,4,5].

node = ListNode.fromList([1,2,3,4,5])
reorderList(node)
print(node.toList())  # [1,5,2,4,3].