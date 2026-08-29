class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 0
        maximumProfit = 0

        while R < len(prices):

            profit = prices[R] - prices[L]                
            maximumProfit = max(profit, maximumProfit)

            if prices[R] < prices[L]:
                L = R
                R += 1
            else:
                R += 1

        return maximumProfit