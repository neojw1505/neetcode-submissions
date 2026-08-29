class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left, right 0 and 1
        l,r = 0, 1
        profit = 0
        while r < len(prices) and l < r:
            # valid left ptr
            if prices[l] <= prices[r]:
                profit = max(profit, prices[r]-prices[l])
                r += 1
            else:
                # find a valid left ptr
                while prices[l] > prices[r]:
                    l += 1
                r = l + 1
        return profit
