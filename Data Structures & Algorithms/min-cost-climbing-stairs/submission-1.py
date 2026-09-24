class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0

        # need to reach n + 1
        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n+1):
            curr_cost = cost[i] if i < n else 0
            dp[i] = min(dp[i-1] + curr_cost, dp[i-2] + curr_cost)
        
        return dp[n]


