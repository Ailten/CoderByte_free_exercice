
# remove duplicates from sorted list two.
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode:
    def __init__(self, val:int=0, next:"ListNode"=None):
        self.val = val
        self.next = next

def func(head: ListNode) -> ListNode:

    if head == None or head.next == None:  # length 0 or 1.
        return head
    if head.next != None and head.next.next == None:  # length 2.
        return None if head.val == head.next.val else head
    
    output_node: ListNode|None = None

    current_node = head
    last_node: ListNode|None = None
    while current_node != None:

        # take current value, and 2 next.
        v = current_node.val
        next_node = current_node.next
        nv = None if next_node == None else next_node.val
        next_next_node = None if next_node == None else next_node.next
        nnv = None if next_next_node == None else next_next_node.val

        if v != nv:
            last_node = current_node
            if output_node == None:
                output_node = current_node
            current_node = current_node.next
            continue

        if v == nnv:  # if all 3 is same, pop the first one.
            if last_node != None:
                last_node.next = next_node
            current_node = current_node.next
        else:  # if only the 2 first are same, pop the 2 first.
            if last_node != None:
                last_node.next = next_next_node
            current_node = current_node.next.next

    return output_node



# ---> example 1.
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(4)
a.next.next.next.next.next = ListNode(4)
a.next.next.next.next.next.next = ListNode(5)
result = func(a)
vals = []
while result != None:
    vals.append(result.val)
    result = result.next
print(vals)  # [1,2,5].

# ---> example 2.
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(1)
a.next.next.next = ListNode(2)
a.next.next.next.next = ListNode(3)
result = func(a)
vals = []
while result != None:
    vals.append(result.val)
    result = result.next
print(vals)  # [2,3].

# ---> example 3.
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(3)
result = func(a)
vals = []
while result != None:
    vals.append(result.val)
    result = result.next
print(vals)  # [1,2].