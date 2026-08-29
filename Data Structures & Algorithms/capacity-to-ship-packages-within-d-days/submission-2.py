class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2
            if self.canShip(weights, days, m):
                r = m
            else:
                l = m + 1
        return r

    def canShip(self, weights, days, capacity):
        curr_load = 0
        curr_day = 1

        for w in weights:
            if curr_load + w > capacity:
                curr_day += 1
                curr_load = w
            else:
                curr_load += w

        return curr_day <= days
        
