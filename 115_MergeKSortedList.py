
# merge k sorted list.
# https://leetcode.com/problems/merge-k-sorted-lists/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def func(nodes : list[ListNode]) -> ListNode:

    output = None
    current_out = None

    # loop until all nodes is None.
    while len(nodes) > 0:
        nodes.sort(key=lambda n: n.val)
        
        if output == None:
            output = ListNode(nodes[0].val)
            current_out = output
        else:
            current_out.next = ListNode(nodes[0].val)
            current_out = current_out.next
        
        nodes[0] = nodes[0].next
        if nodes[0] == None:
            nodes.pop(0)

    return output



# list1 = [1, 2, 3]
list1_ex1 = ListNode(1)
list1_ex1.next = ListNode(2)
list1_ex1.next.next = ListNode(3)
# list2 = [1, 4, 5]
list2_ex1 = ListNode(1)
list2_ex1.next = ListNode(4)
list2_ex1.next.next = ListNode(5)
# list2 = [3, 5, 6]
list3_ex1 = ListNode(3)
list3_ex1.next = ListNode(5)
list3_ex1.next.next = ListNode(6)

result = func([list1_ex1, list2_ex1, list3_ex1])  # --> [1,1,2,3,3,4,5,5,6]
s = []
while True:
    s.append(str(result.val))
    result = result.next
    if result == None:
        break
print(','.join(s))