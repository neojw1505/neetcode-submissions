class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
        # self.buckets
        #   index:  0    1    2    3   ...  999
        #          [ ]  [ ]  [ ]  [ ]      [ ]
        #           ^
        #           each one is its own empty list

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = key % self.size # which bucket 
        if key not in self.buckets[idx]: # sets hold no duplicates
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.size
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % self.size
        if key in self.buckets[idx]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)