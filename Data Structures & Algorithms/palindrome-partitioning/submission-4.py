class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start_index):
            # base case
            if start_index == len(s):
                res.append(path[:])
                return

            # generate all possible substrings
            for i in range(start_index, len(s)):
                sub_string = s[start_index:i+1] 
                if self.is_palindrome(sub_string):
                    path.append(sub_string)
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return res

    def is_palindrome(self, sub):    
        l,r = 0, len(sub)-1
        while l <= r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        return True
