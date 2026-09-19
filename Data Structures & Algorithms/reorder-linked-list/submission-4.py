# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # dummy to point to point to the original head
        dummy = ListNode()
        dummy.next = head

        # 1. split in half, slow and fast
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow ptr will be at mid point 
        curr = slow.next
        slow.next = None # sever the connection to the second list

        # 2. reverse second half of the list 
        prev = None # this will be head of the reversed linked list
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # here the prev is the head of reversed linked list
        head_reversed = prev
        # 3. merge 2 linked list
        while head_reversed and head:
            head_next = head.next
            head_reversed_next = head_reversed.next

            head.next = head_reversed
            head_reversed.next = head_next 

            head = head_next
            head_reversed = head_reversed_next

        print(dummy.next)

    # [0, 1, 2, 3, 4, 5, 6]
    # head: 0 -> 1 -> 2
    # head_reversed: 6 -> 5 -> 4 -> 3
    




