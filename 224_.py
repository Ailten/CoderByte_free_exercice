
# sort list.
# https://leetcode.com/problems/sort-list/

from ListNode import ListNode

def sortList(head: ListNode | None) -> ListNode | None:

    if head == None:
        return None
    
    is_find_un_ordered_elemnt = False
    a = head
    z = None
    while a.next != None:  # browse all nodes (2 by 2).
        b = a.next
        if a.val > b.val:

            if a == head:  # re-define head.
                head = b
                
            c = b.next   # swap.
            b.next = a   # 
            a.next = c   # 
            (a, b) = (b, a)

            if (z != None):  # reconect previous.
                z.next = a

            is_find_un_ordered_elemnt = True

        z = a
        a = b

    # recursive bubble (until browse without changes).
    if is_find_un_ordered_elemnt:
        head = sortList(head)
    
    return head


print(sortList(ListNode.fromList([4,2,1,3])).toList())  # [1,2,3,4].
print(sortList(ListNode.fromList([-1,5,3,4,0])).toList())  # [-1,0,3,4,5].
print(sortList(None))  # None.