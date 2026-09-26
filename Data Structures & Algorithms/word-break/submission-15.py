class Solution:
    """        
            Split Point (j)         End Boundary (i)
                |                       |
                v                       v
    s:   |  l  |  e  |  e  |  t  |  c  |  o  |  d  |  e  |
        └───── Left Piece ──────┘└──── Right Piece ─────┘
                s[0:j]                  s[j:i]
            Checked by:              Checked by:
                dp[j]              s[j:i] in word_set
    """
    # dp[i] represents up to the ith index, i can form that substring [0:i] using words in the word_set
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict) # for O(1) lookup
        max_len = max(len(w) for w in wordDict) if wordDict else 0 
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # "" don't need to match any letters, so True

        for i in range(1, n+1): # O(n)
            for j in range(max(0, i - max_len), i): # O(k)
                if dp[j] == True and s[j:i] in word_set: # O(k)
                    dp[i] = True 
                    break
        return dp[n] 
    # T: O(n*k^2) S: O(n + m*k)
"""
Imagine your dictionary has m = 3 words, but the words are incredibly long (e.g., k = 10,000 letters each).If space complexity were just O(m), it would mean storing those three massive words takes the exact same amount of memory as storing three tiny words like ["a", "b", "c"].

["a", "b", "c"]               --> Storing 3 characters total
["abcdefg...", "hijklmn..."]  --> Storing 30,000 characters total

Because 30,000 bytes is vastly different from 3 bytes, we must include k (the average length of the words) to accurately represent how much memory the computer is using.
"""
