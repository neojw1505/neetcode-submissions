class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # cannot jump
        if s[0] == '1' or s[-1] == '1': return False

        n = len(s)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            if s[i] == '1': continue # cant jump
            for j in range(i+minJump, min(i+maxJump+1, n)):
                if dp[j] == True:
                    dp[i] = True
                    break 
        return dp[0] == True