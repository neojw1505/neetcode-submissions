class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        
        longest = 0
        for i in range(len(s)):
            odd = expand(i,i)    
            even = expand(i,i+1)    
            if len(odd) > longest:
                longest = odd 
            if len(even) > longest:
                longest = even

        return longest