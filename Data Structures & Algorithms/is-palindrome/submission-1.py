class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        # clean up non-alphanumeric char
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                clean_string += ch.lower()
        print(clean_string)

        L, R = 0, len(clean_string) - 1
        while L < R:
            if clean_string[L] != clean_string[R]:
                return False
            L += 1
            R -= 1
        return True