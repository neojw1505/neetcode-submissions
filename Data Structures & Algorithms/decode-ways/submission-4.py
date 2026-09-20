class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0
        res = 0
        prev2 = 1
        prev1 = 1
        # 4 205
        for i in range(1, len(s)):
            res = 0  # reset for current position
            # prefix - last char
            if s[i-1] != "0":
                res += prev1
            # prefix - last 2 char
            if 10 <= int(s[i-1:i+1]) <= 26:
                res += prev2
            prev2,prev1 = prev1,res
        return prev1
