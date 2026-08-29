class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create 2 pointers 
        L, R = 0, 1
        maxProfit = 0

        while R < len(prices):
            # profitable 
            if prices[R] > prices[L]:   
                currPrice = prices[R] - prices[L]
                maxProfit = max(maxProfit, currPrice)
            # not profitable
            else:
                L = R
            R += 1
        return maxProfit