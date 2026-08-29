# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check empty

        if head is None:
            return

        prev = None
        curr = head
        after = curr.next

        while curr is not None:
            curr.next = prev
            prev = curr
            curr = after
            if after is not None:
                after = after.next

        return prev
            