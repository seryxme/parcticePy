from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head_node = ListNode()
        tail_node = ListNode()
        if list1.val <= list2.val:
            head_node.val = list1.val
            list1 = list1.next
        else:
            head_node.val = list2.val
            list2 = list2.next

        tail_node = head_node
        while list1 is not None and list2 is not None:
            mid_node = ListNode()
            if list1.val <= list2.val:
                mid_node = list1
                list1 = list1.next
            else:
                tail_node.next = list1
                list2 = list2.next
            tail_node.next = mid_node
            tail_node = mid_node

        if list1 is not None:
            tail_node.next = list1
        if list2 is not None:
            tail_node.next = list2

        return head_node


lst1 = [1, 2, 4]
lst2 = [1, 3, 4]
print(Solution.mergeTwoLists(lst1, lst2))