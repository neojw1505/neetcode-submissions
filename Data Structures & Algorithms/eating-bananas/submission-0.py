class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating speed, k, range from 1 to max bananas
        L, R = 1, max(piles) 
        minHours = R

        while L <= R:
            # eating speed
            k = (L + R) // 2
            hours = 0
            # loop through piles, calculate hours needed
            # for the current k (eating speed)
            for p in piles:
                hours += math.ceil(p/k)
            # take too long
            if hours > h:
                L = k + 1
            # can finish within h hours
            else:
                # update minHours, try find minimum 
                minHours = min(k, minHours)
                R = k - 1

        return minHours