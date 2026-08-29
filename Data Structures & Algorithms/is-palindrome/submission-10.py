class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # all lowercase
        new_str = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                new_str += ch
        l,r = 0, len(new_str)-1
        while l < r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
        
        return True