# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # phase 1: reach node before position left 
        dummy = ListNode(0, head)
        leftPrev = dummy 
        # left - 1 because want to reach before left position
        for i in range(left - 1):
            leftPrev = leftPrev.next
        
        # phase 2: reverse 
        cur = leftPrev.next 
        prev = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # phase 3: connect
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next 
