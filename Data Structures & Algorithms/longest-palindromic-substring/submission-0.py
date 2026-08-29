class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res