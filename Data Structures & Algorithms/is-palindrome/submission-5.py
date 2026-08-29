class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L,R = 0, len(s)-1
        while L < R:
            if not (s[L].isalpha() or s[L].isnumeric()):
                L += 1
                continue
            if not (s[R].isalpha() or s[R].isnumeric()):
                R -= 1
                continue
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
            elif s[L].lower() != s[R].lower():
                return False
        return True

