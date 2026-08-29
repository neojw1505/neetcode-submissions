# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        l1 = list1
        l2 = list2 
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                temp = l1 
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next
        
        if not l1:
            temp.next = l2
        else:
            temp.next = l1
        
        return dummy.next
