class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size 

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].append(value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.buckets[idx]

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if idx in self.buckets:
            del self.buckets[idx]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)