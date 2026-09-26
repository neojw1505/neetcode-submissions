class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        n = len(coins)
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        # dp[i] = The minimum number of coins needed to make exactly $i change.
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != amount+1 else -1
            

