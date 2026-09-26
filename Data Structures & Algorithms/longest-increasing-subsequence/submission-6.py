class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents the length of the longest increasing subsequence that ends exactly at index i
        n = len(nums)
        dp = [1] * n # every char have at least length 1
        dp[0] = 1

        for i in range(1, n): # O(n)
            for j in range(i): # O(n)
                if nums[j] < nums[i]: # compare nums not dp
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


    # T: O(n^2) S: O(n)