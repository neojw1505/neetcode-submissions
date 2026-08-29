import random
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.arrayList = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.arrayList)
            self.arrayList.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            self.arrayList[self.hashmap[val]] = self.arrayList[-1]
            self.hashmap[self.arrayList[-1]] = self.hashmap[val]
            self.arrayList.pop()
            del self.hashmap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arrayList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()