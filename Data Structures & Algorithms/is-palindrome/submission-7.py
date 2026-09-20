class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        s = s.lower() # all lowercase

        while l < r:
            # check if l and r same
            if not s[l].isalpha():
                l += 1
            
            if not s[r].isalpha():
                r -= 1

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True