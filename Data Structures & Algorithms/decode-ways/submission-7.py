class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1  # Empty string base = 1 way
        dp[1] = 1  # First character is valid = 1 way

        for i in range(2, n + 1):
            dp[i] = 0
            
            # single digit
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            # double digit
            if "10" <= s[i-2 : i] <= "26":
                dp[i] += dp[i-2]
        
        return dp[n]


