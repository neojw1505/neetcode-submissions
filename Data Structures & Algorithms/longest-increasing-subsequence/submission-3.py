class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents the length of the longest increasing subsequence that ends exactly at index i
        n = len(nums)
        dp = [1] * n # every char have at least length 1
        dp[0] = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]
