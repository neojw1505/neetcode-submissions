class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True # "" default to True as no need to match word in wordDict

        # dp[i] -> represents the substr up to the ith index, can be form using the word(s) in the wordDict
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break 
        return dp[n]