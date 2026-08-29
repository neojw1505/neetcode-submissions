# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        l,r = head, head

        while r != None and r.next != None:
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False