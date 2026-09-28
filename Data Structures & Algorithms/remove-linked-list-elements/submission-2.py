# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next # skip it
            else:
                # Step 4: Only move forward if we didn't delete anything
                curr = curr.next
        return dummy.next

    # head=[1, 1]
    # val=1

    # curr = dummy
    # dummy -> 1
