# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        while True:
            
            
            explorer = groupPrev
            for _ in range(k):
                explorer = explorer.next
                if not explorer:
                    return dummy.next

            # step 2: prepare anchors
            groupStart = groupPrev.next
            groupNext = explorer.next

            # step 3: reverse linked list up to next group
            curr = groupStart
            prev = None
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # join the tail of the current group to the next group
            groupStart.next = groupNext
            groupPrev.next = prev
            groupPrev = groupStart
        


            

        
