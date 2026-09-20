class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start_index):
            # base case
            if start_index == len(s):
                res.append(path[:])
                return            

            # choices
            for i in range(start_index, len(s)):
                substring = s[start_index : i + 1]

                if self.is_palindrome(substring):
                    path.append(substring)
                    dfs(i + 1)
                    path.pop()
        dfs(0)
        return res

    def is_palindrome(self, s):
        # accept a string, check if palindrome
        l,r = 0,len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
