class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def expand(l,r):
            count = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            return count 
        
        
        total_palindromes = 0
        
        for i in range(len(s)):
            total_palindromes += expand(i,i)
            total_palindromes += expand(i,i+1)
        
        return total_palindromes