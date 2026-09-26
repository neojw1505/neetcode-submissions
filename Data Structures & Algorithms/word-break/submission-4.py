class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict) # for O(1) lookup

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # "" 

        for i in range(1, n+1): # O(n)
            for j in range(i): # O(n)
                if dp[j] == True and s[j:i] in word_set: # O(n)
                    dp[i] = True 
                    break
        return dp[n] 
    # T: O(n^3) S: O(n)
