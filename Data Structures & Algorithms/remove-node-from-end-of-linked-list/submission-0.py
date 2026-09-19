# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow, fast = head, head
        # fast should have head start of N steps
        for _ in range(n):
            fast = fast.next 

        # edge case: fast can be None if n == len(list)
        # n = 2, list = [1,2], i want to remove 1
        # slow will be pointing to 1, fast will be pointing to None
        if not fast: # fast is None
            return slow.next

        while fast.next: 
            slow = slow.next
            fast = fast.next 
        
        # fast is now at tail, slow is now at the node before the to be removed node
        # BUT i still need the nxt node after the to be removed node
        nxt = slow
        to_be_removed = nxt.next
        nxt = to_be_removed.next # potentially None

        slow.next = nxt # points to the next node
        to_be_removed.next = None # sever the link 

        return dummy.next 


