# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        # find length and tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next 
            length += 1
        
        # connect tail to head
        tail.next = head

        # new tail 
        new_tail = head
        k = k % length
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # new_head 
        new_head = new_tail.next

        # break link
        new_tail.next = None

        head = new_head

        return head

        
