class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = 1000
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        current_bucket = self.buckets[bucket_index]

        for i in range(len(current_bucket)):
            existing_key, existing_val = current_bucket[i]
            if existing_key == key:
                current_bucket[i] = (key, value) 
                return
        current_bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        current_bucket = self.buckets[bucket_index]
        for existing_key, existing_val in current_bucket:
            if existing_key == key:
                return existing_val
        return -1 # Key not found     

    def remove(self, key: int) -> bool:
        bucket_index = self._hash(key)
        current_bucket = self.buckets[bucket_index]

        for i in range(len(current_bucket)):
            existing_key, existing_val = current_bucket[i]
            if existing_key == key:
                current_bucket.pop(i)
                return

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # 1. Double the current capacity limit
        self.capacity = self.capacity * 2
        # 2. Save a temporary copy of our old crowded buckets data
        old_buckets = self.buckets
        # 3. Wipe the main ledger and allocate a brand new, empty, double-sized grid
        self.buckets = [[] for _ in range(self.capacity)]
        # Reset our item counter back to 0
        self.size = 0

        # 4. Migrate the items from the old mailroom into the new one
        for lane in old_buckets:
            for existing_key, existing_val in lane:
                # We re-insert the item! Our insertion method (which we will write next)
                # will automatically calculate its brand-new box address slot.
                self.insert(existing_key, existing_val)




