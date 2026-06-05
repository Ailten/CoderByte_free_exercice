

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 != None:
            return list2
        if list1 != None and list2 == None:
            return list1
        if list1 == None and list2 == None:
            return None

        output = ListNode()
        current_node_output = None

        while list1 != None or list2 != None:

            val1 = float('inf')
            if list1 != None:
                val1 = list1.val
            val2 = float('inf')
            if list2 != None:
                val2 = list2.val

            is_1_lower = val1 < val2
            lower_list = list1 if is_1_lower else list2
            lower_next_value = lower_list.val

            if current_node_output == None:
                output.val = lower_next_value
                current_node_output = output
                if is_1_lower:
                    list1 = list1.next
                else:
                    list2 = list2.next
                continue

            current_node_output.next = ListNode(lower_next_value)
            current_node_output = current_node_output.next
            
            if is_1_lower:
                list1 = list1.next
            else:
                list2 = list2.next

        return output
    

# list1 = [1, 2, 4]
list1_ex1 = ListNode(1)
list1_ex1.next = ListNode(2)
list1_ex1.next.next = ListNode(4)

# list2 = [1, 3, 4]
list2_ex1 = ListNode(1)
list2_ex1.next = ListNode(3)
list2_ex1.next.next = ListNode(4)


s = Solution()
result = s.mergeTwoLists(list1_ex1, list2_ex1)  # 1,1,2,3,4,4
while True:
    print(result.val)
    result = result.next
    if result == None:
        break