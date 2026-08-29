class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for ch in s.lower():
            if ch.isalpha() or ch.isnumeric():
                clean_string += ch
        print(clean_string)    

        L,R = 0, len(clean_string)-1
        while L < R:
            if clean_string[L] == clean_string[R]:
                L += 1
                R -= 1
            else:
                return False
        return True

