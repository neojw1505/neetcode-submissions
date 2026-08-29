# import random
class Solution:

    def __init__(self, w: List[int]):
        total = 0
        self.prefix = []
        for weight in w:
            total += weight
            self.prefix.append(total)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])
        l,r = 0, len(self.prefix)-1
        while l < r:
            m = (l+r)//2
            if self.prefix[m] < target:
                l = m + 1
            else:
                r = m 
        return l 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()