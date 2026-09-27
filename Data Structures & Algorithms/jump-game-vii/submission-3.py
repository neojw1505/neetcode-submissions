class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # cannot jump
        if s[0] == '1' or s[-1] == '1': return False

        n = len(s)
        dp = [False] * n
        dp[n-1] = True
        
        reachable_options += 1

        for i in range(n-2, -1, -1): # O(n)
            # slide left, check new tile at index i+minJump is a valid path
            if i + minJump < n and dp[i + minJump] == True: 
                reachable_options += 1
            # slide right, check the tile at index i+maxJump+1 
            # that fell out from right side is a valid path
            if i + maxJump + 1 < n and dp[i + maxJump+1] == True: 
                reachable_options -= 1
            #. braindead check 
            if s[i] != '1' and reachable_options > 0:
                dp[i] = True

        return dp[0] == True

        # T: O(n) S: O(n)