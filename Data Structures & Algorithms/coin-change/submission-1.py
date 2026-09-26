class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0 # 0 coins needed to change 0 amount

        dp = [amount+1] * (amount+1)
        dp[0] = 0
        dp[1] = amount+1 if 1 not in coins else 1

        for i in range(2, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + (dp[i- coin]))
        return dp[amount] if dp[amount] != amount+1 else -1

