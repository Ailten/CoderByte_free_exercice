
# list node adition (Medium).
# https://leetcode.com/problems/add-two-numbers/

# take two list chained of int, and return a list chained of int (wo represent the adition of both), one digit by cellule.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        output = ListNode(0, None)
        last_node = output

        report = 0
        while True:
            sum_l = l1.val + l2.val + report
            report = sum_l // 10
            value = sum_l % 10
            last_node.val = value
            if l1.next == None or l2.next == None:
                if l1.next == None and l2.next == None:
                    if report != 0:
                        last_node.next = ListNode(report, None)
                    break
                if l1.next == None:
                    l1.next = ListNode(0, None)
                if l2.next == None:
                    l2.next = ListNode(0, None)
            l1 = l1.next
            l2 = l2.next
            last_node.next = ListNode(0, None)
            last_node = last_node.next
        return output

        

