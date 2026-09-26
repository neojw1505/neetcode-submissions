class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                # condition 1    AND  condition 2
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        return dp[n]