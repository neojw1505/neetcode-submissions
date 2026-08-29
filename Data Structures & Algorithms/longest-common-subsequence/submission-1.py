class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. build matrix
        dp = []
        m,n = len(text1), len(text2)
        for i in range(m+1):
            tmp = []
            for j in range(n+1):
                tmp.append(0)
            dp.append(tmp)
        # 2. build dp[i][j]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # match
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                # mismatch
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        
