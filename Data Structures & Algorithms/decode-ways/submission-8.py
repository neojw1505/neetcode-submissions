class Solution:
    def numDecodings(self, s: str) -> int:
        # empty string or leading zero
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 # ""
        dp[1] = 1 if s[0] != "0" else 0  # "1"

        # 12 
        for i in range(2, n+1):
            # check ways as a standalone digit
            if s[i-1] != "0":
                dp[i] += dp[i-1]
                # dp[2] = 1
            # check ways as double digit
            if 10 <= int(s[i-2] + s[i-1]) <= 26: # 12
                dp[i] += dp[i-2]

        return dp[n]
                
