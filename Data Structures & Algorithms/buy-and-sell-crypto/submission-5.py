class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        profit = 0
        while r<len(prices) and l < r:
            if prices[l] < prices[r]:
                profit = max(profit, prices[r]-prices[l])
                r += 1
            else:
                l += 1
                r = l + 1
        return profit
