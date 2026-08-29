class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)

        return self.res