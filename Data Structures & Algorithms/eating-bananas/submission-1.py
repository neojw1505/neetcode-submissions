import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find k, where k = banana eating rate e.g. 2 banana/hr
        # condition 1: total bananas / k < h, for k to be valid
        # condition 2: k * hours >= total bananas
        l = 1
        r = max(piles)
        res = max(piles)
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
            

