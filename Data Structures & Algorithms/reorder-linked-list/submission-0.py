# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. slow and fast ptr get mid point, ends at slow ptr
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 2. reverse the 2nd half of the linkedlist 
        cur = slow
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 3. merge 1st and 2nd half 
        first = head
        second = prev # prev is the head of the 2nd linked list
        while second.next:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            first = tmp1

            second.next = first
            second = tmp2

