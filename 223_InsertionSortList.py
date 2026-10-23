
# Insertion Sort List.
# https://leetcode.com/problems/insertion-sort-list/


from ListNode import ListNode

def insertionSortList(head: ListNode | None) -> ListNode | None:

    if head == None:
        return None

    a = head
    while a != None:

        print(head.toList())

        b = a.next
        if b == None:
            break
        c = b.next

        # disconnect.
        a.next = None
        b.next = None

        # place at index 0.
        if head.val > b.val:
            b.next = head
            if head.next == None:  # if it's two first.
                head.next = c
            else:  # if many ordered before.
                a.next = c
            (head, b) = (b, head)  # replace head.
            continue
        
        # find index to insert.
        else:

            b_i = head
            while b_i != None:
                b_j = b_i.next

                if b_j == None:  # insert at end.
                    b_i.next = b
                    break

                if b_j.val > b.val:  # insert between two.
                    b_i.next = b
                    b.next = b_j
                    break

                b_i = b_j
        
        if a.next == None:  # connect next (if node was insert start or between).
            a.next = c
        elif b.next == None:  # reconnect next (if node was insert end).
            b.next = c
            a = b

    return head



print(insertionSortList(ListNode.fromList([4,2,1,3])).toList())  # [1,2,3,4].
print(insertionSortList(ListNode.fromList([-1,5,3,4,0])).toList())  # [-1,0,3,4,5].
