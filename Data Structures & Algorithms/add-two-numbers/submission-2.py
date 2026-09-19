# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            summ = l1_val + l2_val + carry
            # handle the summ is 2 digits
            if summ >= 10:
                carry = summ // 10
                digit_to_store = summ % 10
                curr = ListNode(digit_to_store) 
            else:
                curr = ListNode(summ)
                carry = 0
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            tail.next = curr
            tail = tail.next
        
        return dummy.next 



