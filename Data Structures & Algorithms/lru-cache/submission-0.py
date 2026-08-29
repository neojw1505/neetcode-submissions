class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        # update to most recent
        self._remove(node) # remove from curr pos in linked list
        self._add(node) # add to last pos in linked list
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node) 
            self._add(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node # put in cache
            self._add(node) # add to linkedlist
        
            if len(self.cache) > self.capacity:
                first = self.head.next
                self._remove(first)
                del self.cache[first.key]

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node