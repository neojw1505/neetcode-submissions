class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, len(prices) - 1
        
        maxProfit = 0
        
        while L < R:
            profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)

            # move left pointer because want to find a smaller 
            if prices[L] >= prices[R]:
                L += 1
            else:
                R -= 1
        
        return maxProfit