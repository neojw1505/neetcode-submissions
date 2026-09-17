class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            profit = prices[r] - prices[l]
            max_profit = max(max_profit,profit)

        return max_profit