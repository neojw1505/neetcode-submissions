# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge sort logic 
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                res.append(self.helperMerge(l1, l2))
            lists = res    
        return lists[0]
    
    # LC easy: merge 2 sorted lists
    def helperMerge(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2 
                l2 = l2.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next