class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        curr_window_end = 0
        farthest = 0
        n = len(s)

        for i in range(len(s)):
            if i > farthest: 
                return False
            if s[i] == "0":
                farthest = max(farthest, i + maxJump)
                curr_window_end = farthest
            if curr_window_end >= n-1:
                return True
        return False