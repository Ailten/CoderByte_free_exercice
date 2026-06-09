
# reverce node K group.
# https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def func(head: ListNode, k: int) -> ListNode:

    node_browse = head
    starting_range_node = head
    i = 0
    range_val = []
    while node_browse != None:
        range_i = i % k

        if range_i == 0 and i > 0:
            for _ in range(k):
                starting_range_node.val = range_val.pop()
                starting_range_node = starting_range_node.next
            range_val.clear()

        range_val.append(node_browse.val)
        node_browse = node_browse.next
        i += 1
    
    return head




# list1 = [1, 2, 3]
list1_ex1 = ListNode(1)
list1_ex1.next = ListNode(2)
list1_ex1.next.next = ListNode(3)
result = func(list1_ex1, 2)  # --> [2, 1, 3]
s = []
while True:
    s.append(str(result.val))
    result = result.next
    if result == None:
        break
print(','.join(s))

# list1 = [1, 2, 3, 4, 5]
list1_ex1 = ListNode(1)
list1_ex1.next = ListNode(2)
list1_ex1.next.next = ListNode(3)
list1_ex1.next.next.next = ListNode(4)
list1_ex1.next.next.next.next = ListNode(5)
result = func(list1_ex1, 2)  # --> [2, 1, 4, 3, 5]
s = []
while True:
    s.append(str(result.val))
    result = result.next
    if result == None:
        break
print(','.join(s))

# list1 = [1, 2, 3, 4, 5]
list1_ex1 = ListNode(1)
list1_ex1.next = ListNode(2)
list1_ex1.next.next = ListNode(3)
list1_ex1.next.next.next = ListNode(4)
list1_ex1.next.next.next.next = ListNode(5)
result = func(list1_ex1, 3)  # --> [3, 2, 1, 4, 5]
s = []
while True:
    s.append(str(result.val))
    result = result.next
    if result == None:
        break
print(','.join(s))


