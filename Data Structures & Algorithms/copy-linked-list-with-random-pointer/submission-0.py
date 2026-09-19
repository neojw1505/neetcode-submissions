"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pass 1: deep copy with old nodes pointing to new nodes 
        #         and new nodes next and random ptrs set to None
        old_to_new = {None: None}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) # dont set next and random, default = None
            curr = curr.next
        
        # pass 2: wire the new nodes next and random pointers by looking at the old list
        curr = head
        while curr:
            old_node_random = curr.random
            old_node_next = curr.next
            new_node = old_to_new[curr]
            new_node.next = old_to_new[old_node_next]
            new_node.random = old_to_new[old_node_random]
            curr = curr.next
        
        return old_to_new[head] 

